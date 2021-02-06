"""Test module for managers."""
import os
import shutil

import pandas as pd

import src.managers as managers


class Test(object):
    """Test class for managers."""

    def setup_method(self, test_method):
        """Remove/create temp dir containing dummy files."""
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testOutDir = os.path.join(self.testHome, "temp_out")
        self.testSource = os.path.join(self.testDir, "managers_test.csv")
        self.testMaster = os.path.join(self.testOutDir, "ftb_managers.txt")

        for obj in [self.testDir, self.testOutDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)
            os.mkdir(obj)

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

        self.testMgrDict = {"test": ["", "managers_test.csv", {}, []]}

        self.testMgrFrame.to_csv(self.testSource, index=False)

        # self.testScrapeOk = {"yay": [self.testSource, os.path.join("temp_scrape.csv"), self.testMgrHeader]}

        # self.testScrapeFail = {
        #     "err": ["does_not_exist.html", "should_not_be_created.csv", ["blah1", "blah2"]]
        # }

    def teardown_method(self, test_method):
        """Remove temp dir containing dummy files."""
        # tear down self.attribute
        for obj in [self.testDir, self.testOutDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)

    # def test_download_managers(self):
    #     """Test for downloading files from web."""
    #     assert managers.download_managers(
    #         managersDict=self.testScrapeOk, directoryIn=self.testDir
    #     )
    #     assert not managers.download_managers(
    #         managersDict=self.testScrapeFail, directoryIn=self.testDir
    #     )

    def test_format_managers(self):
        """Test for formatting managers data."""
        managers.format_managers(
            managersDict=self.testMgrDict,
            directoryIn=self.testDir,
            directoryOut=self.testOutDir,
        )
        assert os.path.isfile(self.testMaster)
