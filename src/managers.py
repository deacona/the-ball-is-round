#!/usr/bin/python -tt
"""
Created on Mon Feb 06 16:49:37 2017

@author: adeacon
"""

import pandas as pd
import datetime
import logging
import config
import utilities

logging.basicConfig(format=config.LOGFORMAT, level=config.LOGLEVEL)

pd.set_option('display.max_columns', 500)
# pd.set_option('display.expand_frame_repr', False)


def _unpack(row, kind="td"):
    elts = row.findAll('%s' % kind)
    return [val.text for val in elts]


def download_managers():
    logging.info("Downloading managers")
    for code, endpoints in config.MANAGERS_SCRAPE.items():
        logging.info("Scraping from {0}".format(endpoints[0]))
        soup = utilities.make_soup(endpoints[0])
        
        table = soup.find('table', attrs=endpoints[2])
        rows = table.findAll('tr')
        
        data = []
        logging.debug(rows[0])
        #logging.debug(_unpack(rows[1], kind=("th")) + _unpack(rows[1], kind=("td"))
        for r in rows:
            data_row = _unpack(r, kind=("th")) + _unpack(r, kind=("td"))
            #logging.debug(data_row
            data.append(data_row)
        
        # logging.debug(data)
        logging.info("Parse clean data")
        dataframe = pd.DataFrame(data[1:],columns=endpoints[3])
        # dataframe.info()
        # logging.debug("Top 20...\n{0}".format(dataframe["Manager"].value_counts()[:20]))

        dataframe['Manager'] = dataframe['Manager'].str.strip()
        logging.debug("Top 20 managers...\n{0}".format(dataframe["Manager"].value_counts()[:20]))
        dataframe['Team'] = dataframe['Team'].str.strip()
        logging.debug("Top 20 teams...\n{0}".format(dataframe["Team"].value_counts()[:20]))
        dataframe['YearRange'] = dataframe['YearRange'].str.strip()
        logging.debug("Top 20 year ranges...\n{0}".format(dataframe["YearRange"].value_counts()[:20]))

        dataframe['DateFrom'] = dataframe['DateFrom'].str.extract('(\d\d [A-Z][a-z]+ \d\d\d\d)', expand=False).str.strip()
        dataframe['DateTo'] = dataframe['DateTo'].str.extract('(\d\d [A-Z][a-z]+ \d\d\d\d)', expand=False).str.strip()

        ## TODO - standardise teams (team names don't match results/stadiums data)

        #dataframe.info()
        #logging.debug(dataframe.describe(include="all"))
        dataframe.to_csv(endpoints[1], encoding='utf-8')
        logging.debug("Retrieve OK: {0}".format(endpoints[:2]))


def format_managers():
    logging.info("Formatting managers")
    pieces = []
    #future_date = datetime.datetime(2099, 12, 31)
    for code, endpoints in config.MANAGERS_SCRAPE.items():
        logging.info("Loading managers data from {0}".format(endpoints[1]))
        dataframe = pd.read_csv(endpoints[1], encoding = "utf8", sep=',', parse_dates=['DateFrom', 'DateTo'])
        pieces.append(dataframe)
    
    logging.info("Concatenate everything into a single DataFrame")
    managers = pd.concat(pieces, ignore_index=True, sort=False)
    managers.drop(['ManagerCountry','Notes','Unnamed: 0'], axis=1, inplace=True)
    #managers['DateFrom'] = managers['DateFrom'].fillna(method='ffill')
    managers['DateTo'] = managers['DateTo'].fillna(datetime.date.today())
    #managers['DateTo'] = managers['DateTo'].fillna(future_date)
    
    logging.info("Fix some missing start dates")
    logging.debug("Before:\n{0}".format(managers[(managers['Manager']=="Peter Taylor") & (managers['Team']=="Hull City")]))
    # managers.set_value(managers[(managers['Manager']=="Peter Taylor") & (managers['Team']=="Hull City")].index.values, 'DateFrom', datetime.datetime(2002, 10, 1))
    managers.at[managers[(managers['Manager']=="Peter Taylor") & (managers['Team']=="Hull City")].index.values, 'DateFrom'] = datetime.datetime(2002, 10, 1)
    logging.debug("After:\n{0}".format(managers[(managers['Manager']=="Peter Taylor") & (managers['Team']=="Hull City")]))
    logging.debug("Before:\n{0}".format(managers[(managers['Manager']=="Ray Lewington") & (managers['Team']=="Watford")]))
    # managers.set_value(managers[(managers['Manager']=="Ray Lewington") & (managers['Team']=="Watford")].index.values, 'DateFrom', datetime.datetime(2002, 6, 1))
    managers.at[managers[(managers['Manager']=="Ray Lewington") & (managers['Team']=="Watford")].index.values, 'DateFrom'] = datetime.datetime(2002, 6, 1)
    logging.debug("After:\n{0}".format(managers[(managers['Manager']=="Ray Lewington") & (managers['Team']=="Watford")]))
    
    #managers.info()
    #logging.debug(managers.describe(include="all"))
    #logging.debug(managers[95:105])
    
    utilities.save_master(managers, "managers")


def main():

    download_managers()
    format_managers()


if __name__ == '__main__':
    main()