#!/usr/bin/python -tt
"""
Created on Mon Feb 06 16:49:37 2017

@author: adeacon
"""

import urllib
import pandas as pd
import logging
import src.config as config
import src.utilities as utilities

logging.basicConfig(format=config.LOGFORMAT, level=config.LOGLEVEL)


def download_stadiums():
    logging.info("Downloading stadiums")
    for code, endpoints in config.STADIUMS_SCRAPE.items():
        try:
            testfile = urllib.URLopener()
            testfile.retrieve(*endpoints)
            logging.debug("retrieve OK: {0}".format(endpoints))
        except:
            logging.warning("retrieve FAILED: {0}".format(endpoints))


def format_stadiums(dgl_file=config.STADIUMS_SCRAPE["dgl"][1], ops_file=config.STADIUMS_SCRAPE["ops"][1], directoryOut=config.MASTER_DIR):
    logging.info("Formatting stadiums")

    # dgl_file = config.STADIUMS_SCRAPE["dgl"][1]
    logging.info("Parsing: {0}".format(dgl_file))
    dgl = pd.read_csv(dgl_file, encoding = "utf8", sep=',')
    dgl.rename(columns={'Name':'Stadium'}, inplace=True)
    dgl.set_index('Team', inplace=True)
    logging.debug("\n{0}".format(dgl))
    
    # ops_file = config.STADIUMS_SCRAPE["ops"][1]
    logging.info("Parsing: {0}".format(ops_file))
    ops = pd.read_csv(ops_file, encoding = "utf8", sep=',')
    ops.rename(columns={'Team':'TeamFull', 'FDCOUK':'Team'}, inplace=True)
    ops.set_index('Team', inplace=True)
    logging.debug("\n{0}".format(ops))

    ## TODO - fuzzy matching teams? (name inconsistencies?)
    
    logging.info("Create combined stadiums data")
    #combo = pd.merge(dgl, ops, left_on='Team', right_on='FDCOUK', how='inner')
    combo = ops.combine_first(dgl)
    combo.reset_index(level=0, inplace=True)
    logging.debug("\n{0}".format(combo))
    
    utilities.save_master(combo, "stadiums", directory=directoryOut)


def main():

    download_stadiums()
    format_stadiums()
   
if __name__ == '__main__':
    main()