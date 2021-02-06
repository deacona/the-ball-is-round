"""Test module for stadiums."""
import os
import shutil

import pandas as pd

import src.stadiums as stadiums


class Test(object):
    """Test class for stadiums."""

    def setup_method(self, test_method):
        """Remove/create temp dir containing dummy files."""
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testOutDir = os.path.join(self.testHome, "temp_out")
        self.testMaster = os.path.join(self.testDir, "ftb_stadiums.txt")

        for obj in [self.testDir, self.testOutDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)
            os.mkdir(obj)

        self.testDGSHeader = [
            "Name",
            "Team",
            "Capacity",
            "Latitude",
            "Longitude",
            "Easting",
            "Northing",
            "Grid Reference",
        ]
        self.testDGSRow = [
            "Abbey Stadium",
            "Cambridge United",
            "10847",
            "52.212799",
            "0.154298",
            "547284",
            "259362",
            "TL472593",
        ]
        self.testDGSFrame = pd.DataFrame(
            data=[self.testDGSRow], columns=self.testDGSHeader
        )
        self.testDGSFile = os.path.join(self.testDir, "stadiums.csv")

        self.testOPSHeader = [
            "Team",
            "FDCOUK",
            "City",
            "Stadium",
            "Capacity",
            "Latitude",
            "Longitude",
            "Country",
        ]
        self.testOPSRow = [
            "Arsenal ",
            "Arsenal",
            "London ",
            "Emirates Stadium ",
            "60361",
            "51.555",
            "-0.108611",
            "England",
        ]
        self.testOPSFrame = pd.DataFrame(
            data=[self.testOPSRow], columns=self.testOPSHeader
        )
        self.testOPSFile = os.path.join(self.testDir, "stadiums_20150302.csv")

        self.testDGSFrame.to_csv(self.testDGSFile, index=False)

        self.testOPSFrame.to_csv(self.testOPSFile, index=False)

        self.testScrapeOk = {"yay": [self.testOPSFile, os.path.join("temp_scrape.csv")]}

        self.testScrapeFail = {
            "err": ["does_not_exist.csv", "should_not_be_created.csv"]
        }

    def teardown_method(self, test_method):
        """Remove temp dir containing dummy files."""
        # tear down self.attribute
        for obj in [self.testDir, self.testOutDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)

    def test_download_stadiums(self):
        """Test for downloading files from web."""
        assert stadiums.download_stadiums(
            scrapeSource=self.testScrapeOk, directoryIn=self.testOutDir
        )
        assert not stadiums.download_stadiums(
            scrapeSource=self.testScrapeFail, directoryIn=self.testOutDir
        )

    def test_format_stadiums(self):
        """Test for formatting stadiums."""
        stadiums.format_stadiums(
            dgl_file=self.testDGSFile,
            ops_file=self.testOPSFile,
            directoryOut=self.testDir,
        )
        assert os.path.isfile(self.testMaster)
