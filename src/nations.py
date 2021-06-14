"""nations module.

Used for national team data
"""

import os

import pandas as pd

import src.config as config
import src.utilities as utilities
from src.utilities import logging


def format_matches(
    directoryOut=config.MASTER_DIR,
):
    """Format national team match data.

    INPUT:
        directoryOut: Directory to save formatted data to

    OUTPUT:
        match: National match data dataframe
    """
    logging.info("Formatting national team match data")

    comp = utilities.folder_loader(
        "fbr",
        "competition",
        source_header=[
            "Round",
            "Wk",
            "Day",
            "Date",
            "Time",
            "Team_1",
            "Score",
            "Team_2",
            "Attendance",
            "Venue",
            "Referee",
            "Match Report",
            "Notes",
        ],
    )
    comp2 = utilities.folder_loader(
        "fbr",
        "competition2",
        source_header=[
            "Round",
            "Wk",
            "Day",
            "Date",
            "Time",
            "Team_1",
            "xG_1",
            "Score",
            "xG_2",
            "Team_2",
            "Attendance",
            "Venue",
            "Referee",
            "Match Report",
            "Notes",
        ],
    )
    comp = pd.concat([comp, comp2], axis=0, sort=False, ignore_index=True)
    comp.dropna(subset=["Round"], inplace=True)
    comp.reset_index(drop=True, inplace=True)
    comp["Year"] = comp.Date.str[:4]
    comp["Team_abbrev_1"] = comp["Team_1"].str[-3:].str.strip()
    comp["Team_1"] = comp["Team_1"].str[:-3].str.strip()
    comp["Team_abbrev_2"] = comp["Team_2"].str[:3].str.strip()
    comp["Team_2"] = comp["Team_2"].str[3:].str.strip()
    comp["Goals_1"] = comp.Score.str.extract(pat="([0-9]{1,2})[^0-9]+[0-9]{1,2}")
    comp["Goals_2"] = comp.Score.str.extract(pat="[0-9]{1,2}[^0-9]+([0-9]{1,2})")
    for i in range(1, 3):
        comp["Goals_" + str(i)] = pd.to_numeric(
            comp["Goals_" + str(i)], errors="coerce"
        )
    comp["Goal_diff"] = comp.Goals_1 - comp.Goals_2
    logging.debug("\n{0}".format(comp.info()))

    venue = pd.read_csv(
        os.path.join(config.SOURCE_DIR, "wkp", "wkp_std", "wkp_std_nat.csv"),
        encoding="latin9",
        sep=",",
    )
    venue.columns = ["Venue_country", "Venue_city", "Venue", "Venue_URL"]
    logging.debug("\n{0}".format(venue.info()))

    match = pd.merge(comp, venue, on="Venue", how="left")

    ## workaround for venues that aren't mapping
    match.loc[match.Venue == "Stadion Energa Gdańsk", "Venue_country"] = "Poland"
    match.loc[match.Venue == "Bakı Olimpiya Stadionu", "Venue_country"] = "Azerbaijan"
    match.loc[match.Venue == "Arena Naţională", "Venue_country"] = "Romania"

    for i in range(1, 3):
        match["Home_" + str(i)] = 0
        match.loc[match["Team_" + str(i)] == match.Venue_country, "Home_" + str(i)] = 1

    logging.debug("\n{0}".format(match.info()))

    utilities.save_master(match, "nations_matches", directory=directoryOut)

    return match


def format_summaries(
    directoryOut=config.MASTER_DIR,
):
    """Format national statistical summary data.

    INPUT:
        directoryOut: Directory to save formatted data to

    OUTPUT:
        None
    """
    logging.info("Formatting national statistical summary data")

    elo_list = []
    for file in os.listdir(os.path.join(config.SOURCE_DIR, "elo")):
        if not file.endswith(".json"):
            continue

        df_json = pd.read_json(os.path.join(config.SOURCE_DIR, "elo", file))
        for i in df_json.index.values:
            df_tmp = pd.DataFrame(df_json.Team[i], index=[i])
            for col in df_tmp.columns.drop("Team"):
                df_tmp[col] = (
                    df_tmp[col].str.replace("−", "-").str.replace("+", "").astype(int)
                )
            df_tmp["Filename"] = file
            df_tmp["Year"] = int(file[:4])
            elo_list.append(df_tmp)

    # print(len(elo_list))

    elo = pd.concat(elo_list, ignore_index=True)

    elo.loc[elo.Team == "Czechia", "Team"] = "Czech Republic"
    elo.loc[elo.Team == "Yugoslavia", "Team"] = "Serbia"
    elo.loc[elo.Team == "Ireland", "Team"] = "Republic of Ireland"
    elo["Country"] = elo.Team
    elo.loc[
        elo.Team.isin(["England", "Scotland", "Wales", "Northern Ireland"]), "Country"
    ] = "United Kingdom"
    elo.loc[(elo.Team == "Russia"), "Country"] = "Russian Federation"

    # elo.describe().T

    penn = pd.read_excel(
        os.path.join(config.SOURCE_DIR, "rug", "pwt100.xlsx"), sheet_name="Data"
    )
    penn = penn[["country", "year", "rgdpe", "pop"]]
    penn.columns = ["Country", "Data Year", "GDP (PPP)", "Population"]
    penn.dropna(axis="index", inplace=True)
    penn.sort_values(by=["Data Year"], inplace=True)
    penn.loc[penn.Country == "Ireland", "Country"] = "Republic of Ireland"
    # penn.info()

    summary = pd.merge_asof(
        elo,
        penn,
        left_by="Country",
        right_by="Country",
        left_on="Year",
        right_on="Data Year",
        tolerance=4,
        allow_exact_matches=False,
    )

    # summary.info()
    utilities.save_master(summary, "nations_summaries", directory=directoryOut)

    return summary


def main():
    """Use the Main for CLI usage."""
    logging.info("Executing nations module")

    format_matches()
    format_summaries()


if __name__ == "__main__":
    main()
