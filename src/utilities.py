#!/usr/bin/python -tt
"""
Created on Tue 06 Nov 2018

@author: adeacon
"""

import os
import pandas as pd
import src.config as config
import requests
from bs4 import BeautifulSoup
import csv


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
    
    #soup = BeautifulSoup(html)
    return BeautifulSoup(html, "lxml")
    #print soup.prettify()

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        return 1
    else:
        return 0

def master_path(stub, directory=config.MASTER_DIR):
    # return config.MASTER_DIR+"/"+"ftb_"+stub+".txt"
    return os.path.join(directory, "ftb_"+stub+".txt")

def get_master(stub, directory=config.MASTER_DIR):
    # print "Fetching "+master_path(stub)
    return pd.read_csv(master_path(stub, directory=directory), encoding = "utf8", sep='|')
    
#    chunksize = 1000
#    chunks = []
#    for chunk in pd.read_csv(master_path(stub), chunksize=chunksize):
#        # Do stuff...
#        chunks.append(chunk)
#    
#    df = pd.concat(chunks, axis=0)
#    return df

def save_master(dframe, stub, directory=config.MASTER_DIR, enc='utf-8'):
    file = master_path(stub, directory=directory)
    dframe.to_csv(file, encoding=enc, sep='|')
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


def folder_loader(source_name, source_header):
    """
    INPUT:
        source_name - String containing name of the data source
        source_name - List of columns in source files
        
    OUTPUT:
        df - Dataframe containing raw loaded data
    """
    
    source_folder = os.path.join(config.SOURCE_DIR, source_name[:3], source_name)
    data_list = []
    for file in os.listdir(source_folder):
        print(file)
        filepath = os.path.join(source_folder, file)
        tmp = pd.read_csv(filepath, encoding='latin-1', header=0, 
                          names=source_header)
        tmp["Season"] = extract_season(file)
        data_list.append(tmp)

    df = pd.concat(data_list, axis=0, sort=False, ignore_index=True)
    
    return df
