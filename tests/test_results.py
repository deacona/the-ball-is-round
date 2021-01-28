#!/usr/bin/python -tt
"""
Created on 23/09/2019

@author: adeacon
"""
import os

import pandas as pd

import src.results as results


class Test(object):
    def setup_method(self, test_method):
        """remove/create temp dir containing dummy files"""
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testCsv = os.path.join(self.testDir, "dummy.csv")
        self.testXlsx = os.path.join(self.testDir, "data.xlsx")
        self.testZip = os.path.join(self.testDir, "data.zip")
        self.testHeader = ["Dummy field 1", "Dummy field 2", "Dummy field 3"]
        self.testRow = ["Bucket", "Filter", "1"]
        self.testFrame = pd.DataFrame.from_dict(
            {
                self.testHeader[0]: [self.testRow[0], self.testRow[0]],
                self.testHeader[1]: [self.testRow[1], self.testRow[1]],
                self.testHeader[2]: [self.testRow[2], self.testRow[2]],
            }
        )
        self.testMaster = os.path.join(self.testDir, "ftb_results.txt")
        self.testBuckets = [self.testHeader[0]]
        self.testStats = self.testHeader[2]
        self.testFilteron = self.testHeader[1]
        self.testValues = [self.testRow[1]]
        self.testAggfunc = "mean"
        # self.testFrameAgg = pd.DataFrame([self.testRow[2]], columns=[self.testAggfunc])
        # self.testFrameAgg.index.name = self.testHeader[0]
        # self.testFrameAgg.rename(index={0:self.testRow[0]},inplace=True)
        self.testAggValue = 1.0
        self.testDiv = [
            {"Div": "EC", "Country": "England", "Tier": 5},
            {"Div": "SC0", "Country": "Scotland", "Tier": 1},
        ]
        self.testDirReal = os.path.join(self.testDir, "1993-1994")
        self.testCsvReal = os.path.join(self.testDirReal, "D1.csv")
        self.testMasterReal = os.path.join(self.testDirReal, "ftb_results.txt")
        self.testHeaderReal = [
            "Div",
            "Date",
            "HomeTeam",
            "AwayTeam",
            "FTHG",
            "FTAG",
            "FTR",
            "HTHG",
            "HTAG",
            "HTR",
            "Attendance",
            "Referee",
            "HS",
            "AS",
            "HST",
            "AST",
            "HHW",
            "AHW",
            "HC",
            "AC",
            "HF",
            "AF",
            "HO",
            "AO",
            "HY",
            "AY",
            "HR",
            "AR",
            "HBP",
            "ABP",
        ]
        self.testRowReal = [
            "D1",
            "07/08/1993",
            "Bayern Munich",
            "Freiburg",
            "3",
            "1",
            "H",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        self.testFrameReal = pd.DataFrame(
            data=[self.testRowReal], columns=self.testHeaderReal
        )

        if os.path.isfile(self.testZip):
            os.remove(self.testZip)

        if os.path.isfile(self.testXlsx):
            os.remove(self.testXlsx)

        if os.path.isfile(self.testCsv):
            os.remove(self.testCsv)

        if os.path.isfile(self.testCsvReal):
            os.remove(self.testCsvReal)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isfile(self.testMasterReal):
            os.remove(self.testMasterReal)

        if os.path.isdir(self.testDirReal):
            os.rmdir(self.testDirReal)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

        os.mkdir(self.testDir)

        os.mkdir(self.testDirReal)

        self.testFrame.to_excel(self.testXlsx)

        self.testFrame.to_csv(self.testCsv)

        self.testFrameReal.to_csv(self.testCsvReal, index=False)

        self.testFrame.to_csv(self.testMaster, sep="|")

    def teardown_method(self, test_method):
        """remove temp dir containing dummy files"""
        # tear down self.attribute
        if os.path.isfile(self.testZip):
            os.remove(self.testZip)

        if os.path.isfile(self.testXlsx):
            os.remove(self.testXlsx)

        if os.path.isfile(self.testCsv):
            os.remove(self.testCsv)

        if os.path.isfile(self.testCsvReal):
            os.remove(self.testCsvReal)

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isfile(self.testMasterReal):
            os.remove(self.testMasterReal)

        if os.path.isdir(self.testDirReal):
            os.rmdir(self.testDirReal)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

    def test_country_and_tier_from_div(self):

        for div in self.testDiv:
            country, tier = results.func_div(div["Div"])
            assert country == div["Country"] and tier == div["Tier"]

    def test_archive_then_unzip_results_files(self):

        assert os.path.isfile(self.testXlsx)
        assert os.path.isfile(self.testCsv)
        assert not (os.path.isfile(self.testZip))

        results.archive_results_files(directory=self.testDir)
        assert not (os.path.isfile(self.testXlsx))
        assert not (os.path.isfile(self.testCsv))
        assert os.path.isfile(self.testZip)

        results.unzip_results_files(directory=self.testDir)
        assert os.path.isfile(self.testXlsx)
        assert not (os.path.isfile(self.testCsv))
        assert not (os.path.isfile(self.testZip))

    # def test_download_results(self):
    #     ''' No test for downloading files from web '''
    #     pass

    def test_format_results(self):
        results.format_results(
            directoryIn=self.testDirReal, directoryOut=self.testDirReal
        )
        assert os.path.isfile(self.testMasterReal)

    def test_results_analysis(self):
        # assert pd.util.testing.assert_frame_equal(results.results_analysis(directory=self.testDir, buckets=self.testBuckets, stats=self.testStats, filteron=self.testFilteron,
        #                                 values=self.testValues, aggfunc=self.testAggfunc),
        #                                 self.testFrameAgg,
        #                                 check_dtype=False,
        #                                 check_less_precise=True,
        #                                 check_names=False,
        #                                 check_index_type=False,
        #                                 check_column_type=False,
        #                                 check_frame_type=False)

        frameValues = results.results_analysis(
            directory=self.testDir,
            buckets=self.testBuckets,
            stats=self.testStats,
            filteron=self.testFilteron,
            values=self.testValues,
            aggfunc=self.testAggfunc,
        ).values
        frameAverage = sum(frameValues) / len(frameValues)
        assert frameAverage == self.testAggValue
