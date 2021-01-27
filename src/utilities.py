#!/usr/bin/python -tt
"""
Created on Tue 06 Nov 2018

@author: adeacon
"""

import os
import shutil
import pandas as pd
import src.config as config
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Arc  # , Rectangle, ConnectionPatch

# from matplotlib.offsetbox import  OffsetImage


def read_header(filepath):
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        i = next(reader)
        # print(i)
        # i = filter(None, i)
        # print(i)
        return i


def make_soup(url):
    response = requests.get(url)
    html = response.content

    # soup = BeautifulSoup(html)
    return BeautifulSoup(html, "lxml")
    # print soup.prettify()


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        return 1
    else:
        return 0


def master_path(stub, directory=config.MASTER_DIR):
    # return config.MASTER_DIR+"/"+"ftb_"+stub+".txt"
    return os.path.join(directory, "ftb_" + stub + ".txt")


def get_master(stub, directory=config.MASTER_DIR):
    # print "Fetching "+master_path(stub)
    return pd.read_csv(master_path(stub, directory=directory), encoding="utf8", sep="|")


#    chunksize = 1000
#    chunks = []
#    for chunk in pd.read_csv(master_path(stub), chunksize=chunksize):
#        # Do stuff...
#        chunks.append(chunk)
#
#    df = pd.concat(chunks, axis=0)
#    return df


def save_master(dframe, stub, directory=config.MASTER_DIR, enc="utf-8"):
    file = master_path(stub, directory=directory)
    dframe.to_csv(file, encoding=enc, sep="|")
    # dframe.to_csv(master_path(stub), sep='|')
    # print "... saved to "+master_path(stub)
    return file


def extract_season(file_name):
    """
    INPUT:
        file_name - String containing name of the data source file

    OUTPUT:
        season_out - String containing the formated label for the season
    """

    season_part = file_name.split(".")[0].split("_")[-1]
    season_out = season_part[:2] + "/" + season_part[-2:]

    return season_out


def extract_competition(file_name):
    """
    INPUT:
        file_name - String containing name of the data source file

    OUTPUT:
        competition_out - String containing the formated label for the competition
    """

    competition_part = file_name.split("_")[3]

    competition_dict = {
        "all": "N/A",
        "chm": "Championship",
        "cpo": "Championship Playoffs",
        "chp": "Championship & Playoffs",
        "fac": "FA Cup",
        "lec": "League Cup",
        "prm": "Premier League",
    }

    competition_out = competition_dict[competition_part]

    return competition_out


def extract_match_id(file_name):
    """
    INPUT:
        file_name - String containing name of the data source file

    OUTPUT:
        match_id - String extracted match_id
    """

    match_id = int(file_name.split("_")[1])

    return match_id


def folder_loader(source_level1, source_level2, file_info=None, source_header=None):
    """
    INPUT:
        source_level1 - Parent folder of data source
        source_level2 - Folder for data source
        file_info - Code for info to extract ffrom filename
        source_header - List of columns in source files

    OUTPUT:
        df - Dataframe containing raw loaded data
    """

    source_folder = os.path.join(config.SOURCE_DIR, source_level1, source_level2)
    data_list = []
    for file in os.listdir(source_folder):
        if not file.endswith(".csv"):
            continue
        print(file)
        filepath = os.path.join(source_folder, file)
        tmp = pd.read_csv(filepath, encoding="latin-1", header=0, names=source_header)
        if file_info == "comp_season":
            tmp["Season"] = extract_season(file)
            tmp["Competition"] = extract_competition(file)
        elif file_info == "match_event":
            tmp["match_id"] = extract_match_id(file)
        data_list.append(tmp)

    df = pd.concat(data_list, axis=0, sort=False, ignore_index=True)

    return df


def draw_pen_box(ax):
    """
    INPUT:
        ax: Existing plot axes

    OUTPUT:
        None
    """
    # size of the pitch is 120, 80

    # Penalty Area
    plt.plot([57.8, 57.8], [120, 105.4], color="black")
    plt.plot([57.8, 22.5], [105.4, 105.4], color="black")
    plt.plot([22.5, 22.5], [120, 105.4], color="black")

    # 6-yard Box
    plt.plot([48, 48], [120, 115.1], color="black")
    plt.plot([48, 32], [115.1, 115.1], color="black")
    plt.plot([32, 32], [120, 115.1], color="black")

    # Penalty spot and the "D"
    topPenSpot = plt.Circle((40, 110.3), 0.71, color="black")
    ax.add_patch(topPenSpot)
    topDArc = Arc(
        (40, 110.3),
        height=16.2,
        width=16.2,
        angle=0,
        theta1=220,
        theta2=320,
        color="black",
    )
    ax.add_patch(topDArc)

    # Goal line
    ax.axhline(y=120, color="black")


def draw_posts(ax):
    """
    INPUT:
        ax: Existing plot axes

    OUTPUT:
        None
    """

    ## 24ft x 8ft
    x1 = 36.0
    x2 = 44.0
    y1 = 0.0
    y2 = (x2 - x1) * 8.0 / 24.0

    x = [x1, x1, x2, x2]
    y = [y1, y2, y2, y1]

    plt.plot(x, y, color="black")
    ax.axhline(y=0, color="black")


def clear_nb_output(outFolder=config.NBOUT_DIR):
    for filename in os.listdir(outFolder):
        file_path = os.path.join(outFolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))
            return False

    return True


def main():

    clear_nb_output()


if __name__ == "__main__":
    main()
