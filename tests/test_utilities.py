#!/usr/bin/python -tt
"""
Created on 23/09/2019

@author: adeacon
"""
import os
import csv
import pandas as pd
import src.utilities as utilities

class Test:

    def setup_method(self, test_method):
        '''remove/create temp dir containing dummy html and csv'''
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testHtml = os.path.join(self.testDir, "dummy.html")
        self.testCsv = os.path.join(self.testDir, "dummy.csv")
        self.testMaster = os.path.join(self.testDir, "ftb_dummy.txt")
        self.testMessage = """<html><head></head><body><p>Hello World!</p></body></html>"""
        self.testHeader = ["Dummy field 1", "Dummy field 2"]
        self.testRow = ["1", "2"]
        self.testFrame = pd.DataFrame(self.testRow, index=self.testHeader)

        if os.path.isfile(self.testHtml):
            os.remove(self.testHtml)

        if os.path.isfile(self.testCsv):
            os.remove(self.testCsv)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

        os.mkdir(self.testDir)

        with open(self.testHtml,'w') as f:
            f.write(self.testMessage)
            f.close()

        with open(self.testCsv, 'a') as f:
            f.write(",".join(self.testHeader)+"\n")
            f.write(",".join(self.testRow)+"\n")


    def teardown_method(self, test_method):
        '''remove temp dir containing dummy html and csv'''
        # tear down self.attribute
        if os.path.isfile(self.testHtml):
            os.remove(self.testHtml)

        if os.path.isfile(self.testCsv):
            os.remove(self.testCsv)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)
                    

    def test_read_header(self):
        '''test returns first line of dummy csv file'''
        # print(utilities.read_header(testCsv))
        assert utilities.read_header(self.testCsv) == self.testHeader


    # def test_make_soup(url):
    #     assert utilities.make_soup(testHtml) == """<html>
    #         <head></head>
    #         <body><p>Hello World!</p></body>
    #         </html>"""


    def test_ensure_dir(self):
        assert utilities.ensure_dir(self.testHtml) == 0


    def test_master_path(self):
        assert utilities.master_path("dummy", directory=self.testDir) == self.testMaster


    def test_get_master(self):
        '''test return dummy dataframe from dummy csv'''
        utilities.save_master(self.testFrame, "dummy", directory=self.testDir)
        utilities.get_master("dummy", directory=self.testDir).shape == self.testFrame.shape


    def test_save_master(self):
        '''test save dummy dataframe to dummy csv'''
        assert utilities.save_master(self.testFrame, "dummy", directory=self.testDir) == self.testMaster
