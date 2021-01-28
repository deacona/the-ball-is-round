#!/usr/bin/python -tt
"""
Created on 17/10/2019

@author: adeacon
"""
import os

import pandas as pd

import src.clubs as clubs


class Test(object):
    def setup_method(self, test_method):
        """remove/create temp dir containing dummy files"""
        # configure self.attribute
        self.testScore = [
            {
                "GoalDiff": -1,
                "Result": "Loss",
                "Points": 0,
                "PointsOpp": 3,
                "Win": 0,
                "WinDraw": 0,
                "Draw": 0,
                "DrawLoss": 1,
                "Loss": 1,
                "WinShare": 0.0,
            },
            {
                "GoalDiff": 10,
                "Result": "Win",
                "Points": 3,
                "PointsOpp": 0,
                "Win": 1,
                "WinDraw": 1,
                "Draw": 0,
                "DrawLoss": 0,
                "Loss": 0,
                "WinShare": 1.0,
            },
        ]

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")
        self.testMaster = os.path.join(self.testDir, "ftb_fulldata.txt")

        self.testBuckets = ["Div"]
        self.testStats = "Goals"
        self.testFilteron = "Team"
        self.testValues = ["Arsenal"]
        self.testAggfunc = "mean"
        self.testAggValue = 9.0 / 5.0

        self.testResultsFile = os.path.join(self.testDir, "ftb_results.txt")
        self.testResultsText = """|Season|Div|Country|Tier|Date|HomeTeam|AwayTeam|FTHG|FTAG|FTR|HTHG|HTAG|HTR|Attendance|Referee|HS|AS|HST|AST|HHW|AHW|HC|AC|HF|AF|HO|AO|HY|AY|HR|AR|HBP|ABP
22512|1997-1998|E0|England|1|1997-08-09|Leeds|Arsenal|1.0|1.0|D|1.0|1.0|D||||||||||||||||||||
22518|1997-1998|E0|England|1|1997-08-11|Arsenal|Coventry|2.0|0.0|H|1.0|0.0|H||||||||||||||||||||
22531|1997-1998|E0|England|1|1997-08-23|Southampton|Arsenal|1.0|3.0|A|1.0|1.0|D||||||||||||||||||||
22540|1997-1998|E0|England|1|1997-08-27|Leicester|Arsenal|3.0|3.0|D|0.0|1.0|A||||||||||||||||||||
22544|1997-1998|E0|England|1|1997-08-30|Arsenal|Tottenham|0.0|0.0|D|0.0|0.0|D||||||||||||||||||||
"""
        self.testManagersFile = os.path.join(self.testDir, "ftb_managers.txt")
        self.testManagersText = """|Manager|Team|DateFrom|DateTo|Duration|YearRange
0|George Graham|Arsenal|1986-05-14|1995-02-21|3205.0|1992-1995
1|Stewart Houston|Arsenal|1995-02-22|2019-02-22|106.0|1995
2|Bruce Rioch|Arsenal||1996-08-12|431.0|1995-1996
3|Stewart Houston|Arsenal|1996-08-12|1996-09-13|32.0|1996
4|Pat Rice|Arsenal|1996-09-13|1996-09-30|17.0|1996
5|Arsene Wenger|Arsenal||2018-05-13|7894.0|1996-2018
6|Unai Emery|Arsenal|2018-05-23|2019-02-22|266.0|2018-
"""
        self.testStadiumsFile = os.path.join(self.testDir, "ftb_stadiums.txt")
        self.testStadiumsText = """|Team|TeamFull|City|Stadium|Capacity|Latitude|Longitude|Country|Easting|Northing|Grid Reference
11|Arsenal|Arsenal |London |Emirates Stadium |60361.0|51.555|-0.108611|England|531236.0|185697.0|TQ312856
"""
        self.testFulldataFile = os.path.join(self.testDir, "ftb_fulldata_in.txt")
        self.testFulldataText = """|Season|Div|Country|Tier|Date|Team|TeamOpp|Goals|GoalsOpp|Goals1stHalf|Goals1stHalfOpp|Attendance|Referee|Shots|ShotsOpp|ShotsOnTarget|ShotsOnTargetOpp|ShotsHitWoodwork|ShotsHitWoodworkOpp|Corners|CornersOpp|Fouls|FoulsOpp|Offsides|OffsidesOpp|YellowCards|YellowCardsOpp|RedCards|RedCardsOpp|BookingPoints|BookingPointsOpp|HomeAway|GoalsDiff|TotalGoals|Goals1stHalfDiff|TotalGoals1stHalf|ShotsDiff|TotalShots|ShotsOnTargetDiff|TotalShotsOnTarget|ShotsHitWoodworkDiff|TotalShotsHitWoodwork|CornersDiff|TotalCorners|FoulsDiff|TotalFouls|OffsidesDiff|TotalOffsides|YellowCardsDiff|TotalYellowCards|RedCardsDiff|TotalRedCards|BookingPointsDiff|TotalBookingPoints|Saves|SavesOpp|SavesDiff|Goals2ndHalf|Goals2ndHalfOpp|Goals2ndHalfDiff|Result|Points|PointsOpp|Win|WinDraw|Draw|DrawLoss|Loss|WinShare|CleanSheet|CleanSheetOpp|GameWeek|City|Stadium|Capacity|Latitude|Longitude|Easting|Northing|Grid Reference|CityOpp|StadiumOpp|CapacityOpp|LatitudeOpp|LongitudeOpp|EastingOpp|NorthingOpp|Grid ReferenceOpp|EuclideanDistance|Manager|ManagerOpp
32196|1997-1998|E0|England|1|1997-08-09|Leeds|Arsenal|1.0|1.0|1.0|1.0|||||||||||||||||||||Home|0.0|2.0|0.0|2.0||||||||||||||||||||||0.0|0.0|0.0|Draw|1|1|0|1|1|1|0|0.0|0|0|1|||||||||London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856|||Stewart Houston
32238|1997-1998|E0|England|1|1997-08-11|Arsenal|Coventry|2.0|0.0|1.0|0.0|||||||||||||||||||||Home|2.0|2.0|1.0|1.0||||||||||||||||||||||1.0|0.0|1.0|Win|3|0|1|1|0|0|0|1.0|0|1|2|London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856||||||||||Stewart Houston|
32345|1997-1998|E0|England|1|1997-08-23|Southampton|Arsenal|1.0|3.0|1.0|1.0|||||||||||||||||||||Home|-2.0|4.0|0.0|2.0||||||||||||||||||||||0.0|2.0|-2.0|Loss|0|3|0|0|0|1|1|0.5|0|0|3|||||||||London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856|||Stewart Houston
32374|1997-1998|E0|England|1|1997-08-27|Leicester|Arsenal|3.0|3.0|0.0|1.0|||||||||||||||||||||Home|0.0|6.0|-1.0|1.0||||||||||||||||||||||3.0|2.0|1.0|Draw|1|1|0|1|1|1|0|0.0|0|0|4|||||||||London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856|||Stewart Houston
32475|1997-1998|E0|England|1|1997-08-30|Arsenal|Tottenham|0.0|0.0|0.0|0.0|||||||||||||||||||||Home|0.0|0.0|0.0|0.0||||||||||||||||||||||0.0|0.0|0.0|Draw|1|1|0|1|1|1|0|0.0|1|1|5|London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856||||||||||Stewart Houston|
368723|1997-1998|E0|England|1|1997-08-09|Arsenal|Leeds|1.0|1.0|1.0|1.0|||||||||||||||||||||Away|0.0|2.0|0.0|2.0||||||||||||||||||||||0.0|0.0|0.0|Draw|1|1|0|1|1|1|0|0.0|0|0|1|London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856||||||||||Stewart Houston|
368761|1997-1998|E0|England|1|1997-08-11|Coventry|Arsenal|0.0|2.0|0.0|1.0|||||||||||||||||||||Away|-2.0|2.0|-1.0|1.0||||||||||||||||||||||0.0|1.0|-1.0|Loss|0|3|0|0|0|1|1|0.5|1|0|2|||||||||London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856|||Stewart Houston
368823|1997-1998|E0|England|1|1997-08-23|Arsenal|Southampton|3.0|1.0|1.0|1.0|||||||||||||||||||||Away|2.0|4.0|0.0|2.0||||||||||||||||||||||2.0|0.0|2.0|Win|3|0|1|1|0|0|0|1.0|0|0|3|London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856||||||||||Stewart Houston|
368893|1997-1998|E0|England|1|1997-08-27|Arsenal|Leicester|3.0|3.0|1.0|0.0|||||||||||||||||||||Away|0.0|6.0|1.0|1.0||||||||||||||||||||||2.0|3.0|-1.0|Draw|1|1|0|1|1|1|0|0.0|0|0|4|London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856||||||||||Stewart Houston|
368929|1997-1998|E0|England|1|1997-08-30|Tottenham|Arsenal|0.0|0.0|0.0|0.0|||||||||||||||||||||Away|0.0|0.0|0.0|0.0||||||||||||||||||||||0.0|0.0|0.0|Draw|1|1|0|1|1|1|0|0.0|1|1|5|||||||||London |Emirates Stadium |60361.0|51.555|-0.108611|531236.0|185697.0|TQ312856|||Stewart Houston
"""

        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isfile(self.testResultsFile):
            os.remove(self.testResultsFile)

        if os.path.isfile(self.testManagersFile):
            os.remove(self.testManagersFile)

        if os.path.isfile(self.testStadiumsFile):
            os.remove(self.testStadiumsFile)

        if os.path.isfile(self.testFulldataFile):
            os.remove(self.testFulldataFile)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

        os.mkdir(self.testDir)

        with open(self.testResultsFile, "a") as the_file:
            the_file.write(self.testResultsText)

        with open(self.testManagersFile, "a") as the_file:
            the_file.write(self.testManagersText)

        with open(self.testStadiumsFile, "a") as the_file:
            the_file.write(self.testStadiumsText)

        with open(self.testFulldataFile, "a") as the_file:
            the_file.write(self.testFulldataText)

    def teardown_method(self, test_method):
        """remove temp dir containing dummy files"""
        # tear down self.attribute
        if os.path.isfile(self.testMaster):
            os.remove(self.testMaster)

        if os.path.isfile(self.testResultsFile):
            os.remove(self.testResultsFile)

        if os.path.isfile(self.testManagersFile):
            os.remove(self.testManagersFile)

        if os.path.isfile(self.testStadiumsFile):
            os.remove(self.testStadiumsFile)

        if os.path.isfile(self.testFulldataFile):
            os.remove(self.testFulldataFile)

        if os.path.isdir(self.testDir):
            os.rmdir(self.testDir)

    def test_func_score(self):
        for score in self.testScore:
            assert (
                score["Result"],
                score["Points"],
                score["PointsOpp"],
                score["Win"],
                score["WinDraw"],
                score["Draw"],
                score["DrawLoss"],
                score["Loss"],
                score["WinShare"],
            ) == clubs.func_score(score["GoalDiff"])

    def test_func_nogoal(self):
        for goal in range(0, 10):
            if goal == 0:
                assert clubs.func_nogoal(goal) == 1
            else:
                assert clubs.func_nogoal(goal) == 0

    def test_build_fulldata(self):
        fulldataIn = pd.read_csv(self.testFulldataFile, sep="|", index_col=0)
        fulldataOut = clubs.build_fulldata(directory=self.testDir)
        assert fulldataIn.shape == fulldataOut.shape

    def test_fulldata_analysis(self):
        clubs.build_fulldata(directory=self.testDir)
        frameValues = clubs.fulldata_analysis(
            directory=self.testDir,
            buckets=self.testBuckets,
            stats=self.testStats,
            filteron=self.testFilteron,
            values=self.testValues,
            aggfunc=self.testAggfunc,
        ).values
        frameAverage = sum(frameValues) / len(frameValues)
        assert frameAverage == self.testAggValue

    def test_get_summary(self):
        fulldataIn = pd.read_csv(self.testFulldataFile, sep="|", index_col=0)
        summaryValues = clubs.get_summary(
            "".join(self.testBuckets),
            df=fulldataIn,
            agg_method="mean",
            base_filters={self.testFilteron: self.testValues},
            output_metrics=[self.testStats],
        ).values
        assert summaryValues == self.testAggValue
