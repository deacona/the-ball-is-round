#!/usr/bin/python -tt
"""
Created on Mon Feb 06 16:49:37 2017

@author: adeacon
"""

import os
import urllib
import pandas as pd
import numpy as np
import logging
import zipfile
import src.config as config
import src.utilities as utilities

logging.basicConfig(format=config.LOGFORMAT, level=config.LOGLEVEL)

pd.set_option('display.max_columns', 50)
#pd.set_option('display.expand_frame_repr', False)

#cd ../data/source/ftd
#for i in {0..23}; do mkdir $((1993+i))-$((1994+i)); done

def download_results():
    logging.info("Downloading results")

    remotepath =  os.path.dirname(config.RESULTS_SCRAPE["ftd"][0])    
    soup = utilities.make_soup(config.RESULTS_SCRAPE["ftd"][0])
    logging.info("Scrape list of zip files from {0}".format(config.RESULTS_SCRAPE["ftd"][0]))
    
    for table in soup.findAll('table', attrs={'cellspacing': '2', 'border': '0'}):
        for item in table.findAll('a', href=True):
            #logging.info(item.text)
            #logging.info(item['href'])
        
            remotefile = remotepath+"/"+item['href']
            logging.info("Remote file: {0}".format(remotefile))
            
            localfile = config.RESULTS_SCRAPE["ftd"][1]+"/"+item.text.replace("Season ","").replace("/","-")+"/"+os.path.basename(item['href'])
            logging.info("Local file: {0}".format(localfile))
    
            utilities.ensure_dir(localfile)
            
            testfile = urllib.request.URLopener()
            testfile.retrieve(remotefile, localfile)
            logging.info("Retrieve OK: "+str([remotefile, localfile]))


def unzip_results_files(directory=config.RESULTS_SCRAPE["ftd"][1]):
    logging.info("Unzipping results files")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "data.zip":
                #logging.info(root)
                #logging.info(dirs)
                #logging.info(file)
                file_to_unzip = os.path.join(root, file)
                logging.info("File to unzip: {0}".format(file_to_unzip))
                with zipfile.ZipFile(file_to_unzip,"r") as zip_ref:
                    zip_ref.extractall(root)
                os.remove(file_to_unzip)


def func_div(x):
    div_dict = {
        'B1': ['Belgium',1]
        , 'D1': ['Germany',1]
        , 'D2': ['Germany',2]
        , 'E0': ['England',1]
        , 'E1': ['England',2]
        , 'E2': ['England',3]
        , 'E3': ['England',4]
        , 'EC': ['England',5]
        , 'F1': ['France',1]
        , 'F2': ['France',2]
        , 'G1': ['Greece',1]
        , 'I1': ['Italy',1]
        , 'I2': ['Italy',2]
        , 'N1': ['Holland',1]
        , 'P1': ['Portugal',1]
        , 'SC0': ['Scotland',1]
        , 'SC1': ['Scotland',2]
        , 'SC2': ['Scotland',3]
        , 'SC3': ['Scotland',4]
        , 'SP1': ['Spain',1]
        , 'SP2': ['Spain',2]
        , 'T1': ['Turkey',1]
        }
    return div_dict[x]


def format_results(directoryIn=config.RESULTS_SCRAPE["ftd"][1], directoryOut=config.MASTER_DIR):
    logging.info("Format results")
    pieces = []
    core_cols = ['Div','Date'] #,'HomeTeam','AwayTeam','FTHG','FTAG','FTR']
    use_cols = ['Season','Div','Country','Tier','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Attendance','Referee','HS','AS','HST','AST','HHW','AHW','HC','AC','HF','AF','HO','AO','HY','AY','HR','AR','HBP','ABP']

    for root, dirs, files in os.walk(directoryIn):
        for file in files:
            if file.endswith(".csv"):
                #logging.info(root)
                filepath = os.path.join(root, file)
                logging.info("Filepath: {0}".format(filepath))
                #logging.info(root[-9:])
                # try:
                df = pd.read_csv(filepath, error_bad_lines=False, warn_bad_lines=False, encoding="latin9") #, parse_dates=['Date'])
                logging.debug("Input columns: {0}".format(df.columns))
                #df['File'] = file
                df['Season'] = root[-9:]

                if set(["HomeTeam", "AwayTeam"]).issubset(df.columns):
                    # logging.info(df[["HomeTeam", "AwayTeam"]].head())
                    try:
                        df["HomeTeam"] = df["HomeTeam"] #.apply(lambda x: x.decode('latin9').encode('utf-8'))
                        df["AwayTeam"] = df["AwayTeam"] #.apply(lambda x: x.decode('latin9').encode('utf-8'))
                    except:
                        df["HomeTeam"] = np.nan
                        df["AwayTeam"] = np.nan

                elif set(["HT", "AT"]).issubset(df.columns):
                    # logging.info(df[["HT", "AT"]].head())
                    try:
                        df["HomeTeam"] = df["HT"] #.apply(lambda x: x.decode('latin9').encode('utf-8'))
                        df["AwayTeam"] = df["AT"] #.apply(lambda x: x.decode('latin9').encode('utf-8'))
                    except:
                        df["HomeTeam"] = np.nan
                        df["AwayTeam"] = np.nan
                else:
                    raise
                # logging.info(df[["HomeTeam", "AwayTeam"]].head())

                #drop useless rows
                df = df.dropna(subset=core_cols)
                logging.debug("Output columns: {0}".format(df.columns))

                pieces.append(df)
                # except:
                #     logging.info("read_csv FAILED: "+os.path.join(root, file))
                #logging.info(df.count())
    
    logging.info("Concatenate everything into a single DataFrame")
    dframe = pd.concat(pieces, ignore_index=True, sort=False)
    
    dframe['Country'], dframe['Tier'] = zip(*dframe['Div'].map(func_div))

    # dframe["Date"] = pd.to_datetime(dframe['Date'], format='%d/%m/%y')
    dframe.Date = pd.to_datetime(dframe.Date,dayfirst=True)
    logging.info(dframe[use_cols].info())

    # logging.info(dframe[((dframe['HomeTeam']=="Middlesbrough")|(dframe['AwayTeam']=="Middlesbrough"))&(dframe['Season']=="2006-2007")][["Date", "HomeTeam", "AwayTeam"]])
    utilities.save_master(dframe[use_cols], "results", directory=directoryOut) #, enc="ascii")
    #return dframe[use_cols]


def archive_results_files(directory=config.RESULTS_SCRAPE["ftd"][1]):
    logging.info("Removing/zipping unzipped results files from {0}".format(directory))
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_to_delete = os.path.join(root, file)
                logging.info("File to delete: {0}".format(file_to_delete))
                os.remove(file_to_delete)
            elif file.endswith((".xls", ".xlsx")):
                file_to_zip = os.path.join(root, file)
                file_as_zip = os.path.splitext(file_to_zip)[0]+'.zip'
                logging.info("File to zip: {0}".format((file_to_zip, file_as_zip)))
                with zipfile.ZipFile(file_as_zip, 'w') as myzip:
                    myzip.write(file_to_zip, file)
                os.remove(file_to_zip)


def results_analysis(directory=config.MASTER_DIR, buckets=['Div','Season'], stats=('HS','AS','HST','AST','FTHG','FTAG'), 
                        filteron='HomeTeam', values=['Barcelona'], aggfunc='mean'):
    logging.info("Results analysis")

    dframe = utilities.get_master("results", directory)

    # dframe.info()
    # dframe.describe(include="all")
    # print(dframe)

    # buckets = ['Div','Season']
    # stats = 'HS','AS','HST','AST','FTHG','FTAG'
    # filteron = 'HomeTeam'
    # values = ['Barcelona']
    # aggfunc = 'mean'

    pseudocode = "SELECT "+aggfunc+" OF "+str(stats)+" WHERE "+filteron+" IS "+str(values)+" GROUPED BY "+str(buckets)
    logging.info("Analysis pseudocode: {0}".format(pseudocode))
    
    selected = dframe[dframe[filteron].isin(values)].groupby(buckets)[stats].agg([aggfunc])

    # print(selected)
    logging.info(selected.describe(include="all"))
    # pd.scatter_matrix(selected, diagonal='kde')
    #plt.show()

    return selected


def main():

    download_results() ## Some dates wrong???
    unzip_results_files()
    format_results() ## SOME TEAM NAMES DO NOT LOAD/PARSE
    archive_results_files()
    results_analysis()


if __name__ == '__main__':
    main()