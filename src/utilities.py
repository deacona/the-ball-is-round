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
    with open(filepath, "rb") as f:
        reader = csv.reader(f)
        i = reader.next()
        i = filter(None, i)
        # print i
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
    dframe.to_csv(master_path(stub, directory=directory), encoding=enc, sep='|')
    # dframe.to_csv(master_path(stub), sep='|')
    # print "... saved to "+master_path(stub)
