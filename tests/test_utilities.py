#!/usr/bin/python -tt
"""
Created on 23/09/2019

@author: adeacon
"""
import os
import csv
import pandas as pd
import src.utilities as utilities

testHome = "tests"
testDir = os.path.join(testHome, "temp")
testHtml = os.path.join(testDir, "dummy.html")
testCsv = os.path.join(testDir, "dummy.csv")
testMaster = os.path.join(testDir, "ftb_dummy.txt")
testMessage = """<html><head></head><body><p>Hello World!</p></body></html>"""
testHeader = ["Dummy field 1", "Dummy field 2"]
testRow = ["1", "2"]
testFrame = pd.DataFrame(testRow, index=testHeader)


class Test:

    def setup_method(self, test_method):
        '''remove/create temp dir containing dummy html and csv'''
        # configure self.attribute
        if os.path.isfile(testHtml):
            os.remove(testHtml)

        if os.path.isfile(testCsv):
            os.remove(testCsv)

        if os.path.isfile(testMaster):
            os.remove(testMaster)

        if os.path.isdir(testDir):
            os.rmdir(testDir)

        os.mkdir(testDir)

        with open(testHtml,'w') as f:
            f.write(testMessage)
            f.close()

        with open(testCsv, 'a') as f:
            f.write(",".join(testHeader)+"\n")
            f.write(",".join(testRow)+"\n")


    def teardown_method(self, test_method):
        '''remove temp dir containing dummy html and csv'''
        # tear down self.attribute
        if os.path.isfile(testHtml):
            os.remove(testHtml)

        if os.path.isfile(testCsv):
            os.remove(testCsv)

        if os.path.isfile(testMaster):
            os.remove(testMaster)

        if os.path.isdir(testDir):
            os.rmdir(testDir)
                    

    def test_read_header(self):
        '''test returns first line of dummy csv file'''
        # print(utilities.read_header(testCsv))
        assert utilities.read_header(testCsv) == testHeader


    # def test_make_soup(url):
    #     assert utilities.make_soup(testHtml) == """<html>
    #         <head></head>
    #         <body><p>Hello World!</p></body>
    #         </html>"""


    def test_ensure_dir(self):
        assert utilities.ensure_dir(testHtml) == 0


    def test_master_path(self):
        assert utilities.master_path("dummy", directory=testDir) == testMaster


    def test_get_master(self):
        '''test return dummy dataframe from dummy csv'''
        utilities.save_master(testFrame, "dummy", directory=testDir)
        utilities.get_master("dummy", directory=testDir).shape == testFrame.shape


    def test_save_master(self):
        '''test save dummy dataframe to dummy csv'''
        assert utilities.save_master(testFrame, "dummy", directory=testDir) == testMaster
