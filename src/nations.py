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
    comp.dropna(subset=["Round"], inplace=True)
    comp.reset_index(drop=True, inplace=True)
    comp["Year"] = comp.Date.str[:4]
    comp["Team_abbrev_1"] = comp["Team_1"].str[-2:]
    comp["Team_1"] = comp["Team_1"].str[:-3]
    comp["Team_abbrev_2"] = comp["Team_2"].str[:2]
    comp["Team_2"] = comp["Team_2"].str[3:]
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

    return


def main():
    """Use the Main for CLI usage."""
    logging.info("Executing nations module")

    format_matches()
    format_summaries()


if __name__ == "__main__":
    main()
