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

    logging.debug(competition_id, event_type)
    comps = pd.read_csv(os.path.join(config.SOURCE_DIR, "stb", "competitions", "competitions_None.csv"))
    season_ids = comps[comps.competition_id == competition_id].season_id.values

    for season_id in season_ids:
        logging.debug(season_id)
        mats = pd.read_csv(os.path.join(config.SOURCE_DIR, "stb", "matches", "matches_{0}_{1}.csv".format(competition_id, season_id)))
        match_ids = mats.match_id.values

        os.chdir(os.path.join(config.SOURCE_DIR, "stb", "events"))
        for match_id in match_ids:
            logging.debug(match_id)
            sb.Events(event_id=str(match_id)).save_data(event_type=event_type)

    return


def build_event_data(competition_id, event_type, directory=config.MASTER_DIR):
    """Building event data

    Args:
        event_type: String value of event type
        directory: Folder for processed data

    Returns:
        None
    """
    logging.info("Building event data")

    comps = utilities.folder_loader("stb", "competitions")
    print(comps.info())
    matches = utilities.folder_loader("stb", "matches")
    print(matches.info())
    events = utilities.folder_loader("stb", "events", "match_event")
    print(events.info())

    data = comps.loc[comps.competition_id == competition_id, ["season_id","country_name","competition_name","season_name"]]\
        .merge(matches.loc[matches.competition == competition_id, ["match_id","match_date","kick_off","season"]], 
            how="inner", left_on="season_id", right_on="season")\
        .merge(events.loc[:, ["event_type","period","minute","team","player","statsbomb_xg","type","outcome",
            "start_location_x","start_location_y","end_location_x","end_location_y","end_location_z","match_id"]],
            how="inner", on="match_id")
    print(data.info())        

    utilities.save_master(data, "events_{0}".format(event_type), directory=directory)

    return data


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
    build_event_data(competition_id=11, event_type="shot")


if __name__ == '__main__':
    main()
