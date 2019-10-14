#!/usr/bin/python -tt
"""
Created on 23/09/2019

@author: adeacon
"""
import os
import pandas as pd
import src.results as results

testHome = "tests"
testDir = os.path.join(testHome, "temp")
testCsv = os.path.join(testDir, "dummy.csv")
testXlsx = os.path.join(testDir, "data.xlsx")
testZip = os.path.join(testDir, "data.zip")
testHeader = ["Dummy field 1", "Dummy field 2", "Dummy field 3"]
testRow = ["Bucket", "Filter", "1"]
testFrame = pd.DataFrame.from_dict({
    testHeader[0]: [testRow[0],testRow[0]],
    testHeader[1]: [testRow[1],testRow[1]],
    testHeader[2]: [testRow[2],testRow[2]],
})
testMaster = os.path.join(testDir, "ftb_results.txt")
testBuckets = [testHeader[0]]
testStats = (testHeader[2])
testFilteron = testHeader[1]
testValues = [testRow[1]]
testAggfunc = 'mean'
testFrameAgg = pd.DataFrame([testRow[2]], columns=[testAggfunc])
testFrameAgg.index.name = testHeader[0]
testFrameAgg.rename(index={0:testRow[0]},inplace=True)


class Test(object):

    def setup_method(self, test_method):
        '''remove/create temp dir containing dummy files'''
        # configure self.attribute
        if os.path.isfile(testZip):
            os.remove(testZip)

        if os.path.isfile(testXlsx):
            os.remove(testXlsx)

        if os.path.isfile(testCsv):
            os.remove(testCsv)

        if os.path.isfile(testMaster):
            os.remove(testMaster)

        if os.path.isdir(testDir):
            os.rmdir(testDir)

        os.mkdir(testDir)

        testFrame.to_excel(testXlsx)

        testFrame.to_csv(testCsv)

        testFrame.to_csv(testMaster, sep='|')


    def teardown_method(self, test_method):
        '''remove temp dir containing dummy files'''
        # tear down self.attribute
        if os.path.isfile(testZip):
            os.remove(testZip)

        if os.path.isfile(testXlsx):
            os.remove(testXlsx)

        if os.path.isfile(testCsv):
            os.remove(testCsv)

        if os.path.isfile(testMaster):
            os.remove(testMaster)

        if os.path.isdir(testDir):
            os.rmdir(testDir)


    def test_country_and_tier_from_div(self):
        
        country, tier = results.func_div("EC")
        assert country == "England" and tier == 5
        
        country, tier = results.func_div("SC0")
        assert country == "Scotland" and tier == 1
    

    def test_archive_then_unzip_results_files(self):

        assert (os.path.isfile(testXlsx))
        assert (os.path.isfile(testCsv))
        assert not (os.path.isfile(testZip))
        
        results.archive_results_files(directory=testDir)
        assert not (os.path.isfile(testXlsx))
        assert not (os.path.isfile(testCsv))
        assert (os.path.isfile(testZip))

        results.unzip_results_files(directory=testDir)
        assert (os.path.isfile(testXlsx))
        assert not (os.path.isfile(testCsv))
        assert not (os.path.isfile(testZip))


    # def test_download_results(self):
    #     ''' No test for downloading files from web '''
    #     pass

    def test_format_results(self):
        pass

    def test_results_analysis(self):
        assert pd.util.testing.assert_frame_equal(results.results_analysis(directory=testDir, buckets=testBuckets, stats=testStats, filteron=testFilteron, 
                                        values=testValues, aggfunc=testAggfunc), testFrameAgg, check_dtype=False)


