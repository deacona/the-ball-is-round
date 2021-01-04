"""events module

Used for any event related data processing
"""

import statsbomb as sb
import os
import pandas as pd
import logging
import src.config as config
import src.utilities as utilities

logging.basicConfig(format=config.LOGFORMAT, level=config.LOGLEVEL)


def download_competitions():
    """Download all competition data for events

    Args:
        None

    Returns:
        None
    """
    logging.info("Downloading event competitions")
    
    os.chdir(os.path.join(config.SOURCE_DIR, "stb", "competitions"))
    sb.Competitions().save_data()

    return


def download_matches(competition_id):
    """Download all match data for events

    Args:
        competition_id: Id of competition

    Returns:
        None
    """
    logging.info("Downloading event matches")

    comps = pd.read_csv(os.path.join(config.SOURCE_DIR, "stb", "competitions", "competitions_None.csv"))
    season_ids = comps[comps.competition_id == competition_id].season_id.values
    
    os.chdir(os.path.join(config.SOURCE_DIR, "stb", "matches"))
    for season_id in season_ids:
        mats = sb.Matches(event_id=competition_id, season_id=season_id)
        mats.save_data()

    return


def download_events(competition_id, event_type):
    """Download all event data

    Args:
        competition_id: Id of competition
        event_type: String value of event type

    Returns:
        None
    """
    logging.info("Downloading events")

    comps = pd.read_csv(os.path.join(config.SOURCE_DIR, "stb", "competitions", "competitions_None.csv"))
    season_ids = comps[comps.competition_id == competition_id].season_id.values

    for season_id in season_ids:
        mats = pd.read_csv(os.path.join(config.SOURCE_DIR, "stb", "matches", "matches_{0}_{1}.csv".format(competition_id, season_id)))
        match_ids = mats.match_id.values

        os.chdir(os.path.join(config.SOURCE_DIR, "stb", "events"))
        for match_id in match_ids:
            sb.Events(event_id=str(match_id)).save_data(event_type=event_type)

    return


def main():
    """Sequence functions for use in data pipeline

    Args:
        None

    Returns:
        None
    """

    download_competitions()
    download_matches(competition_id=11)
    download_events(competition_id=11, event_type="shot")


if __name__ == '__main__':
    main()
