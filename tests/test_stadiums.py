#!/usr/bin/python -tt
"""
Created on 16/10/2019

@author: adeacon
"""
import os
import pandas as pd
import src.stadiums as stadiums


class Test(object):

    def setup_method(self, test_method):
        '''remove/create temp dir containing dummy files'''
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testMaster = os.path.join(self.testDir, "ftb_stadiums.txt")

        self.testDGSHeader = ['Name','Team','Capacity','Latitude','Longitude','Easting','Northing','Grid Reference']
        self.testDGSRow = ['Abbey Stadium','Cambridge United','10847','52.212799','0.154298','547284','259362','TL472593']
        self.testDGSFrame = pd.DataFrame(data=[self.testDGSRow], columns = self.testDGSHeader)
        self.testDGSFile = os.path.join(self.testDir, "stadiums.csv")

        self.testOPSHeader = ['Team','FDCOUK','City','Stadium','Capacity','Latitude','Longitude','Country']
        self.testOPSRow = ['Arsenal ','Arsenal','London ','Emirates Stadium ','60361','51.555','-0.108611','England']
        self.testOPSFrame = pd.DataFrame(data=[self.testOPSRow], columns = self.testOPSHeader)
        self.testOPSFile = os.path.join(self.testDir, "stadiums_20150302.csv")

        if os.path.isfile(self.testDGSFile):
            os.remove(self.testDGSFile)

        if os.path.isfile(self.testOPSFile):
            os.remove(self.testOPSFile)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

        os.mkdir(self.testDir)

        self.testDGSFrame.to_csv(self.testDGSFile, index=False)

        self.testOPSFrame.to_csv(self.testOPSFile, index=False)


    def teardown_method(self, test_method):
        '''remove temp dir containing dummy files'''
        # tear down self.attribute
        if os.path.isfile(self.testDGSFile):
            os.remove(self.testDGSFile)

        if os.path.isfile(self.testOPSFile):
            os.remove(self.testOPSFile)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

    # def test_download_stadiums(self):
    #     ''' No test for downloading files from web '''
    #     pass

    def test_format_stadiums(self):
        stadiums.format_stadiums(dgl_file=self.testDGSFile, ops_file=self.testOPSFile, directoryOut=self.testDir)
        assert (os.path.isfile(self.testMaster))

