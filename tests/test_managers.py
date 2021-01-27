#!/usr/bin/python -tt
"""
Created on 17/10/2019

@author: adeacon
"""
import os
import pandas as pd
import src.managers as managers


class Test(object):
    def setup_method(self, test_method):
        """remove/create temp dir containing dummy files"""
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testSource = os.path.join(self.testDir, "managers_test.csv")
        self.testMaster = os.path.join(self.testDir, "ftb_managers.txt")

        self.testMgrHeader = [
            "Manager",
            "ManagerCountry",
            "Team",
            "DateFrom",
            "DateTo",
            "Duration",
            "YearRange",
            "Notes",
            "Unnamed: 0",
        ]
        self.testMgrRow = [
            "George Graham",
            """
""",
            "Arsenal",
            "14-May-86",
            "21-Feb-95",
            """3205
""",
            "1992â€“1995",
            "",
            "",
        ]
        self.testMgrFrame = pd.DataFrame(
            data=[self.testMgrRow], columns=self.testMgrHeader
        )

        self.testMgrDict = {"test": ["", self.testSource, {}, []]}

        if os.path.isfile(self.testSource):
            os.remove(self.testSource)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

        os.mkdir(self.testDir)

        self.testMgrFrame.to_csv(self.testSource, index=False)

    def teardown_method(self, test_method):
        """remove temp dir containing dummy files"""
        # tear down self.attribute
        if os.path.isfile(self.testSource):
            os.remove(self.testSource)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

    # def test_download_managers(self):
    #     ''' No test for downloading files from web '''
    #     pass

    def test_format_managers(self):
        managers.format_managers(
            managersDict=self.testMgrDict, directoryOut=self.testDir
        )
        assert os.path.isfile(self.testMaster)
