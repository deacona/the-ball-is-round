"""Test module for nations."""
import os
import shutil

import src.nations as nations


class Test(object):
    """Test class for nations."""

    def setup_method(self, test_method):
        """Remove/create temp dir containing dummy files."""
        # configure self.attribute
        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testMaster1 = os.path.join(self.testDir, "ftb_nations_matches.txt")
        self.testMaster2 = os.path.join(self.testDir, "ftb_nations_summaries.txt")

        for obj in [self.testDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)

        for obj in [self.testDir]:
            os.mkdir(obj)

    def teardown_method(self, test_method):
        """Remove temp dir containing dummy files."""
        # tear down self.attribute
        for obj in [self.testDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)

    def test_format_matches(self):
        """Test for format_matches."""
        assert nations.format_matches(directoryOut=self.testDir).shape[0] > 200
        assert os.path.isfile(self.testMaster1)

    def test_format_summaries(self):
        """Test for format_summaries."""
        assert nations.format_summaries(directoryOut=self.testDir).shape[0] > 0
        assert os.path.isfile(self.testMaster2)
