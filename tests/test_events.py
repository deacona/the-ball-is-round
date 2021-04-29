"""Test module for events."""
import statsbomb as sb

# import src.events as events


class Test(object):
    """Test class for config."""

    def setup_method(self, test_method):
        """Prepare method events Test class."""
        # configure self.attribute
        self.comps = sb.Competitions().get_dataframe()
        self.mats = sb.Matches(event_id="11", season_id="1").get_dataframe()
        self.events = sb.Events(event_id="9948").get_dataframe(event_type="shot")

    def teardown_method(self, test_method):
        """Teardown method for events Test class."""
        # tear down self.attribute
        self.comps = None
        self.mats = None
        self.events = None

    def test_download_competitions(self):
        """Test events.download_competitions."""
        assert self.comps.shape[0] >= 16
        assert self.comps.shape[1] == 8

    def test_download_matches(self):
        """Test events.download_matches."""
        assert self.mats.shape[0] == 36
        assert self.mats.shape[1] == 18

    def test_download_events(self):
        """Test events.download_events."""
        assert self.events.shape[0] == 25
        assert self.events.shape[1] == 33


# def test_build_event_data(self):
#         """Test events.build_event_data."""
