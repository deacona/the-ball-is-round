"""Test module for config."""

import os

import src.config as config


class Test(object):
    """Test class for config."""

    def test_object_types(self):

        for obj in [
            config.HOME_DIR,
            config.SOURCE_DIR,
            config.MASTER_DIR,
            config.NBOUT_DIR,
        ]:
            assert isinstance(obj, str)

        for obj in [
            config.RESULTS_SCRAPE,
            config.STADIUMS_SCRAPE,
            config.MANAGERS_SCRAPE,
        ]:
            assert isinstance(obj, dict)

    def test_dirs_exist(self):

        for folder in [
            config.HOME_DIR,
            config.SOURCE_DIR,
            config.MASTER_DIR,
            config.NBOUT_DIR,
        ]:
            assert os.path.exists(folder)
