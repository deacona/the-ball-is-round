#!/usr/bin/python -tt
"""
Created on 23/09/2019

@author: adeacon
"""
from src.results import func_div


class TestResults(object):

    def test_country_and_tier_from_div(self):
        
        country, tier = func_div("EC")
        assert country == "England" and tier == 5
        
        country, tier = func_div("SC0")
        assert country == "Scotland" and tier == 1
