"""stadium module.

Used for any stadium data processes
"""

import os

import pandas as pd

import src.config as config
import src.utilities as utilities
from src.utilities import logging


def download_stadiums(
    scrapeSource=config.STADIUMS_SCRAPE, directoryIn=config.SOURCE_DIR
):
    """Download stadiums data.

    INPUT:
        scrapeSource: Info on scraped data
        directoryIn: Location to download to

    OUTPUT:
        Boolean: True if download ok, False otherwise
    """
    logging.info("Downloading stadiums")
    for _code, endpoints in scrapeSource.items():
        try:
            df = pd.read_csv(endpoints[0])
            df.to_csv(os.path.join(directoryIn, endpoints[1]), index=False)
            logging.info("retrieve OK: {0}".format(endpoints))
            return True
        except Exception as e:
            logging.warning("retrieve FAILED: {0}".format(endpoints))
            logging.error(e)
            return False


def format_stadiums(
    dgl_file=config.STADIUMS_SCRAPE["dgl"][1],
    ops_file=config.STADIUMS_SCRAPE["ops"][1],
    directoryOut=config.MASTER_DIR,
):
    """Format stadiums data.

    INPUT:
        dgl_file: Path for "dgl" stadiums file
        ops_file: Path for "ops" stadiums file
        directoryOut: Direcory to save formatted data to

    OUTPUT:
        None
    """
    logging.info("Formatting stadiums")

    # dgl_file = config.STADIUMS_SCRAPE["dgl"][1]
    logging.info("Parsing: {0}".format(dgl_file))
    dgl = pd.read_csv(dgl_file, encoding="utf8", sep=",")
    dgl.rename(columns={"Name": "Stadium"}, inplace=True)
    dgl.set_index("Team", inplace=True)
    logging.debug("\n{0}".format(dgl))

    # ops_file = config.STADIUMS_SCRAPE["ops"][1]
    logging.info("Parsing: {0}".format(ops_file))
    ops = pd.read_csv(ops_file, encoding="utf8", sep=",")
    ops.rename(columns={"Team": "TeamFull", "FDCOUK": "Team"}, inplace=True)
    ops.set_index("Team", inplace=True)
    logging.debug("\n{0}".format(ops))

    ## TODO - fuzzy matching teams? (name inconsistencies?)

    logging.info("Create combined stadiums data")
    # combo = pd.merge(dgl, ops, left_on='Team', right_on='FDCOUK', how='inner')
    combo = ops.combine_first(dgl)
    combo.reset_index(level=0, inplace=True)
    logging.debug("\n{0}".format(combo))

    utilities.save_master(combo, "stadiums", directory=directoryOut)

    return


def main():
    """Use the Main for CLI usage."""
    logging.info("Executing stadiums module")

    download_stadiums()
    format_stadiums()


if __name__ == "__main__":
    main()
