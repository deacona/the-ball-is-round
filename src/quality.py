"""data quality module.

Used for any data quality processes
"""
import datetime
import os

import pandas as pd

import src.config as config
import src.utilities as utilities
from src.utilities import logging


def calculate_quality(directory=config.MASTER_DIR):
    """Calculate data quality.

    INPUT:
        directory: Location of data to assess

    OUTPUT:
        overall_score: Overall quality score across all files
    """
    logging.info("Calculating data quality")

    calc_date = datetime.datetime.today().strftime("%Y-%m-%d")
    logging.info("Current date is {0}".format(calc_date))

    dq_data = []
    for file in os.listdir(directory):
        if file == "ftb_quality.txt":
            continue
        if not file.endswith(".txt"):
            continue
        logging.info("Assessing {0}".format(file))

        file_path = os.path.join(directory, file)

        file_date = datetime.datetime.fromtimestamp(
            os.path.getmtime(file_path)
        ).strftime("%Y-%m-%d")
        logging.info("File modification date is {0}".format(calc_date))

        file_stub = file.replace("ftb_", "").replace(".txt", "")
        df = utilities.get_master(file_stub, directory=directory).sample(
            frac=0.1, replace=False, random_state=42
        )

        no_of_rows, no_of_columns = df.shape
        no_of_cells = no_of_rows * no_of_columns

        # Consistency, coherence, or clarity
        category = "Consistency"
        logging.info("Running {0} tests".format(category))

        # DOB < Joined date < Contract date
        # Goals <= SoT <= Shots

        # Completeness or comprehensiveness
        category = "Completeness"
        logging.info("Running {0} tests".format(category))

        test = "Missing values"
        score = df.count().sum() / no_of_cells
        dq_data.append(
            {
                "file": file_stub,
                "file_date": file_date,
                "calc_date": calc_date,
                "category": category,
                "test": test,
                "score": score,
            }
        )

        # Timeliness or latency
        category = "Timeliness"
        logging.info("Running {0} tests".format(category))

        test = "Days since file updated"
        score = max(
            1
            - (
                (int(calc_date.replace("-", "")) - int(file_date.replace("-", "")))
                / 100000
            ),
            0,
        )
        dq_data.append(
            {
                "file": file_stub,
                "file_date": file_date,
                "calc_date": calc_date,
                "category": category,
                "test": test,
                "score": score,
            }
        )

        date_field = None
        if file in ["ftb_fulldata.txt", "ftb_results.txt"]:
            date_field = "Date"
        elif file in ["ftb_events_shot.txt"]:
            date_field = "match_date"
        elif file in ["ftb_managers.txt"]:
            date_field = "DateTo"

        if date_field:
            test = "Days since last match date"
            score = max(
                1
                - (
                    (
                        int(calc_date.replace("-", ""))
                        - int(df[date_field].max().replace("-", ""))
                    )
                    / 100000
                ),
                0,
            )
            dq_data.append(
                {
                    "file": file_stub,
                    "file_date": file_date,
                    "calc_date": calc_date,
                    "category": category,
                    "test": test,
                    "score": score,
                }
            )

        # Accuracy or correctness
        category = "Accuracy"
        logging.info("Running {0} tests".format(category))

        # Spots tests against ref data?
        # Wikipedia (Ajax, Frankfurt)
        # Don Balon (Spain 08/09)
        # SkySports Football Yearbook (England & Scotland 07/08)

        # Uniqueness
        category = "Uniqueness"
        logging.info("Running {0} tests".format(category))

        test = "Duplicated rows"
        score = df.drop_duplicates().shape[0] / no_of_rows
        dq_data.append(
            {
                "file": file_stub,
                "file_date": file_date,
                "calc_date": calc_date,
                "category": category,
                "test": test,
                "score": score,
            }
        )

        test = "Duplicated columns"
        score = df.T.drop_duplicates().T.shape[0] / no_of_rows
        dq_data.append(
            {
                "file": file_stub,
                "file_date": file_date,
                "calc_date": calc_date,
                "category": category,
                "test": test,
                "score": score,
            }
        )

        # Validity or reasonableness
        category = "Validity"
        logging.info("Running {0} tests".format(category))

        # 0 <= Goals <= 10

        test = "3 stdev from mean"
        score = 1 - (
            ((df < (df.mean() - 3 * df.std())) | (df > df.mean() + 3 * df.std()))
            .sum()
            .sum()
            / no_of_cells
        )
        dq_data.append(
            {
                "file": file_stub,
                "file_date": file_date,
                "calc_date": calc_date,
                "category": category,
                "test": test,
                "score": score,
            }
        )

        test = "1.5 IQR rule"
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        score = 1 - (
            ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum().sum()
            / no_of_cells
        )
        dq_data.append(
            {
                "file": file_stub,
                "file_date": file_date,
                "calc_date": calc_date,
                "category": category,
                "test": test,
                "score": score,
            }
        )

        # Orderliness
        # Auditability
        # Conformity
        # accessibility or availability
        # comparability
        # credibility, reliability, or reputation
        # relevance, pertinence, or usefulness

    df_dq = pd.DataFrame(dq_data)
    utilities.save_master(df_dq, "quality", directory=directory)

    overall_score = df_dq.score.mean()
    logging.info("Overall score is {0}".format(overall_score))

    return overall_score


def main():
    """Use the Main for CLI usage."""
    logging.info("Executing data quality module")

    calculate_quality()


if __name__ == "__main__":
    main()
