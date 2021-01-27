"""test_events module

Used for testing of event related data processing
"""

import statsbomb as sb
import src.events as events


class Test(object):
    def setup_method(self, test_method):
        """setup method for events Test class

        Args:
            self
            test_method

        Returns:
            None
        """
        # configure self.attribute
        self.comps = sb.Competitions().get_dataframe()
        self.mats = sb.Matches(event_id="11", season_id="1").get_dataframe()
        self.events = sb.Events(event_id="9948").get_dataframe(event_type="shot")

    def teardown_method(self, test_method):
        """teardown method for events Test class

        Args:
            self
            test_method

        Returns:
            None
        """
        # tear down self.attribute
        self.comps = None
        self.mats = None
        self.events = None

    def test_download_competitions(self):
        """test events.download_competitions

        Args:
            self

        Returns:
            None
        """
        assert self.comps.shape[0] >= 16
        assert self.comps.shape[1] == 8

    def test_download_matches(self):
        """test events.download_matches

        Args:
            self

        Returns:
            None
        """
        assert self.mats.shape[0] == 36
        assert self.mats.shape[1] == 16

    def test_download_events(self):
        """test events.download_events

        Args:
            self

        Returns:
            None
        """
        assert self.events.shape[0] == 25
        assert self.events.shape[1] == 33


# def test_build_event_data(self):
#         """test events.build_event_data

#         Args:
#             self

#         Returns:
#             None
#         """
