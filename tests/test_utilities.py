"""Test module for utilities."""
import os
import shutil

import matplotlib.pyplot as plt
import pandas as pd

import src.utilities as utilities


class Test:
    """Test class for config."""

    def setup_method(self, test_method):
        """Remove/create temp objects."""
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testHtml = os.path.join(self.testDir, "dummy.html")
        self.testSubDir = os.path.join(self.testDir, "temp_sub")
        self.testSubDirFile = os.path.join(self.testSubDir, "dummy.txt")
        self.testCsv = os.path.join(self.testDir, "dummy.csv")
        self.testMaster = os.path.join(self.testDir, "ftb_dummy.txt")
        self.testMessage = (
            """<html><head></head><body><p>Hello World!</p></body></html>"""
        )
        self.testHeader = ["Dummy field 1", "Dummy field 2"]
        self.testRow = ["1", "2"]
        self.testFrame = pd.DataFrame(self.testRow, index=self.testHeader)
        self.testFilename = "tmk_cnt_mbr_all_0910.csv"
        self.testSeason = "09/10"
        self.testCompetition = "N/A"
        self.testFilename2 = "events_10_test.csv"
        self.testMatchId = 10
        self.testOutDir = os.path.join(self.testHome, "temp_out")
        self.testOutFile = os.path.join(self.testOutDir, "dummy.md")

        self.plt = plt
        self.ax = plt.gca()

        for obj in [self.testDir, self.testOutDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)
            os.mkdir(obj)

        with open(self.testHtml, "w") as f:
            f.write(self.testMessage)
            f.close()

        with open(self.testCsv, "a") as f:
            f.write(",".join(self.testHeader) + "\n")
            f.write(",".join(self.testRow) + "\n")
            f.close()

        with open(self.testOutFile, "w") as f:
            f.close()

    def teardown_method(self, test_method):
        """Remove temp objects."""
        # tear down self.attribute
        for obj in [self.testDir, self.testOutDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)

    def test_read_header(self):
        """Test returns first line of dummy csv file."""
        # print(utilities.read_header(testCsv))
        assert utilities.read_header(self.testCsv) == self.testHeader

    # def test_make_soup(url):
    #     assert utilities.make_soup(testHtml) == """<html>
    #         <head></head>
    #         <body><p>Hello World!</p></body>
    #         </html>"""

    def test_ensure_dir(self):
        """Test ensure dir exists."""
        assert utilities.ensure_dir(self.testOutFile) == 0
        assert utilities.ensure_dir(self.testSubDirFile) == 1

    def test_master_path(self):
        """Test build master filepath."""
        assert utilities.master_path("dummy", directory=self.testDir) == self.testMaster

    def test_get_master(self):
        """Test return dummy dataframe from dummy csv."""
        utilities.save_master(self.testFrame, "dummy", directory=self.testDir)
        utilities.get_master(
            "dummy", directory=self.testDir
        ).shape == self.testFrame.shape

    def test_save_master(self):
        """Test save dummy dataframe to dummy csv."""
        assert (
            utilities.save_master(self.testFrame, "dummy", directory=self.testDir)
            == self.testMaster
        )

    def test_extract_season(self):
        """Test extract season from filename."""
        assert utilities.extract_season(self.testFilename) == self.testSeason

    def test_extract_competition(self):
        """Test extract competition from filename."""
        assert utilities.extract_competition(self.testFilename) == self.testCompetition

    def test_extract_match_id(self):
        """Test extract match_id from filename."""
        assert utilities.extract_match_id(self.testFilename2) == self.testMatchId

    # def test_folder_loader(self):
    # '''test loading source files in folder'''
    # assert blah

    def test_draw_pen_box(self):
        """Test drawing penalty box on plot."""
        assert utilities.draw_pen_box(self.plt, self.ax)

    def test_draw_posts(self):
        """Test drawing goal posts on plot."""
        assert utilities.draw_posts(self.plt, self.ax)

    def test_clear_nb_output(self):
        """Test clearing notebook output."""
        assert utilities.clear_nb_output(self.testOutDir)
