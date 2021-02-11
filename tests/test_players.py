"""Test module for players."""
# import os
# import shutil

# import pandas as pd

import src.players as players


class Test(object):
    """Test class for players."""

    def setup_method(self, test_method):
        """Remove/create temp dir containing dummy files."""
        # configure self.attribute
        pass
        # for obj in [self.testWkpMgrDir, self.testWkpDir, self.testDir, self.testOutDir]:
        #     if os.path.isdir(obj):
        #         shutil.rmtree(obj)

        # for obj in [self.testDir, self.testWkpDir, self.testWkpMgrDir, self.testOutDir]:
        #     os.mkdir(obj)

    def teardown_method(self, test_method):
        """Remove temp dir containing dummy files."""
        # tear down self.attribute
        pass
        # for obj in [self.testWkpMgrDir, self.testWkpDir, self.testDir, self.testOutDir]:
        #     if os.path.isdir(obj):
        #         shutil.rmtree(obj)

    def test_get_outfile(self):
        """Test for returning outfile stub."""
        assert players.get_outfile("tmk_cnt") == "players_contract"
        assert players.get_outfile("tmk_psm") == "players_performance"

    # def test_clean_data(self):
    #     """Test for formatting players data."""
    #     players.clean_data()
