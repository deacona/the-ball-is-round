#!/usr/bin/python -tt
"""

@author: adeacon
"""

import os
import configparser

conf = configparser.RawConfigParser()
conf.read('..\src\config.ini')

SOURCE_DIR = os.path.join(conf["PROJECT"]["HOMEDIR"], "data", "raw")
MASTER_DIR = os.path.join(conf["PROJECT"]["HOMEDIR"], "data", "processed")

#code: remoteurl, localfile
RESULTS_SCRAPE = {
        "ftd": ["http://football-data.co.uk/downloadm.php",
                os.path.join(SOURCE_DIR, "ftd")]
}

#code: remoteurl, localfile
STADIUMS_SCRAPE = {
        "ops": ["http://opisthokonta.net/wp-content/uploads/2015/03/stadiums_20150302.csv",
                os.path.join(SOURCE_DIR, "ops", "stadiums", "stadiums_20150302.csv")]
        , "dgl": ["https://www.doogal.co.uk/FootballStadiumsCSV.ashx",
                os.path.join(SOURCE_DIR, "dgl", "stadiums", "stadiums.csv")]
        }

#code: remoteurl, localfile, attrs
MANAGERS_SCRAPE = {
        "prm": ["https://en.wikipedia.org/wiki/List_of_Premier_League_managers",
                os.path.join(SOURCE_DIR, "wkp", "wkp_mgr", "wkp_mgr_prm.csv"),
                {'class': 'wikitable sortable plainrowheaders'},
                ['Manager','ManagerCountry','Team','DateFrom','DateTo','Duration','YearRange','Notes']]
                #,{'Name': 'Manager','Nat.': 'ManagerCountry', 'Club': 'Team','From': 'DateFrom','Until': 'DateTo','Duration (days)': 'Duration','"Years in\r\nPremier League"': 'YearRange','Ref.': 'Notes'}]
        , "chm": ["https://en.wikipedia.org/wiki/List_of_EFL_Championship_managers",
                os.path.join(SOURCE_DIR, "wkp", "wkp_mgr", "wkp_mgr_chm.csv"),
                {'class': 'wikitable sortable'},
                ['Manager','ManagerCountry','Team','DateFrom','DateTo','YearRange','Notes']]
                #,{'Name': 'Manager','Nat.': 'ManagerCountry','Championship club': 'Team','From': 'DateFrom','Until': 'DateTo','"Years in\r\nFLC"': 'YearRange','Ref.': 'Notes'}]
        }
