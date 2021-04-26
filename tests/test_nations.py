"""Test module for nations."""
# import os
# import shutil

# import pandas as pd

import src.nations as nations


class Test(object):
    """Test class for nations."""

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

    def test_format_matches(self):
        """Test for format_matches."""
        assert 1 == 0

