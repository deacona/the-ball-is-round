#!/usr/bin/python -tt
"""
Created on Mon Feb 06 16:49:37 2017

@author: adeacon
"""

import requests
import os
import urllib
import pandas as pd
import config
import utilities

#pd.set_option('display.max_columns', 500)
#pd.set_option('display.expand_frame_repr', False)

#cd ../data/source/ftd
#for i in {0..23}; do mkdir $((1993+i))-$((1994+i)); done

def download_results():
    #print "scrape list of zip files from url"
    remotepath =  os.path.dirname(config.RESULTS_SCRAPE["ftd"][0])
    
    soup = utilities.make_soup(config.RESULTS_SCRAPE["ftd"][0])
    
    for table in soup.findAll('table', attrs={'cellspacing': '2', 'border': '0'}):
        for item in table.findAll('a', href=True):
            #print item.text
            #print item['href']
        
            remotefile = remotepath+"/"+item['href']
            #print remotefile
            
            localfile = config.RESULTS_SCRAPE["ftd"][1]+"/"+item.text.replace("Season ","").replace("/","-")+"/"+os.path.basename(item['href'])
            #print localfile
            
            utilities.ensure_dir(localfile)
            
            testfile = urllib.URLopener()
            testfile.retrieve(remotefile, localfile)
            print "retrieve OK: "+str([remotefile, localfile])

def download_stadiums():
    for code, endpoints in config.STADIUMS_SCRAPE.items():
        try:
            testfile = urllib.URLopener()
            testfile.retrieve(*endpoints)
            print "retrieve OK: "+str(endpoints)
        except:
            print "retrieve FAILED: "+str(endpoints)

def _unpack(row, kind="td"):
    elts = row.findAll('%s' % kind)
    return [val.text for val in elts]

def download_managers():
    for code, endpoints in config.MANAGERS_SCRAPE.items():
        soup = utilities.make_soup(endpoints[0])
        
        table = soup.find('table', attrs=endpoints[2])
        rows = table.findAll('tr')
        
        data = []
        print rows[0]
        #print _unpack(rows[1], kind=("th")) + _unpack(rows[1], kind=("td"))
        for r in rows:
            data_row = _unpack(r, kind=("th")) + _unpack(r, kind=("td"))
            #print data_row
            data.append(data_row)
            
        print data
        dataframe = pd.DataFrame(data[1:],columns=endpoints[3])
        dataframe['Manager'] = dataframe['Manager'].str.split(',', 1).str[1].str.extract('([A-Z][a-z]+)[A-Z]', expand=False).str.strip() +" "+ dataframe['Manager'].str.extract('([a-zA-Z ]+)', expand=False).str.strip()
        dataframe['DateFrom'] = dataframe['DateFrom'].str.extract('(\d\d [A-Z][a-z]+ \d\d\d\d)', expand=False).str.strip()
        dataframe['DateTo'] = dataframe['DateTo'].str.extract('(\d\d [A-Z][a-z]+ \d\d\d\d)', expand=False).str.strip()
        #dataframe.info()
        #print dataframe.describe(include="all")
        dataframe.to_csv(endpoints[1], encoding='utf-8')
        print "retrieve OK: "+str(endpoints[:2])

def main():

    download_results() ## Some dates wrong???
    download_stadiums()
    download_managers() # manually correcting line breaks
 
if __name__ == '__main__':
    main()