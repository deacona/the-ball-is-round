"""Test module for quality."""
import os
import shutil

import src.quality as quality


class Test(object):
    """Test class for quality."""

    def setup_method(self, test_method):
        """Remove/create temp dir containing dummy files."""
        # configure self.attribute

        self.testHome = "tests"
        self.testDir = os.path.join(self.testHome, "temp")

        self.testFulldataFile = os.path.join(self.testDir, "ftb_fulldata.txt")
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

        for obj in [self.testDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)
            os.mkdir(obj)

        with open(self.testFulldataFile, "a") as the_file:
            the_file.write(self.testFulldataText)

    def teardown_method(self, test_method):
        """Remove temp dir containing dummy files."""
        # tear down self.attribute
        for obj in [self.testDir]:
            if os.path.isdir(obj):
                shutil.rmtree(obj)

    def test_calculate_quality(self):
        """Test for calculating data quality."""
        assert 0.7 < quality.calculate_quality(directory=self.testDir) < 1.0
