#!/usr/bin/python -tt
"""
Created on 23/09/2019

@author: adeacon
"""
import src.config as config


class TestConfig(object):

    def test_object_types(self):

        assert isinstance(config.SOURCE_DIR, str)

        assert isinstance(config.MASTER_DIR, str)

        assert isinstance(config.RESULTS_SCRAPE, dict)

        assert isinstance(config.STADIUMS_SCRAPE, dict)

        assert isinstance(config.MANAGERS_SCRAPE, dict)
