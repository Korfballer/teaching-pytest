"""Test utility functions."""

# Standard library imports
import datetime

# Third party imports
import pytest
from pandas import Timestamp
from superhelpful.utilities import is_working_hours

# Local application imports
# n/a


class TestIsWorkingHours:
    """Test is_working_hours function."""

    @pytest.mark.parametrize(
        "value",
        (
            # Sunday 1 January 2023
            datetime.datetime(year=2023, month=1, day=1),
            # Monday 2 January 2023 @ 8am
            datetime.datetime(year=2023, month=1, day=2, hour=8),
            # Tuesday 3 January 2023 @ 5pm
            datetime.datetime(year=2023, month=1, day=3, hour=17),
            # Wednesday 4 January 2023 @ 7pm
            Timestamp(year=2023, month=1, day=4, hour=19),
            # 8am
            datetime.time(hour=8),
            # Saturday 7 January 2023
            Timestamp(year=2023, month=1, day=7)))
    def test_out_of_hours(self, value):
        """Test cases that are OUTSIDE of working hours."""
        actual = is_working_hours(value=value)

        expected = False

        assert actual == expected

    @pytest.mark.parametrize(
        "value",
        (
            # Monday 2 January 2023
            datetime.datetime(year=2023, month=1, day=2, hour=12),
            # Tuesday 3 January 2023 @ 9am
            datetime.datetime(year=2023, month=1, day=3, hour=9),
            # Wednesday 4 January 2023 @ 5pm
            datetime.datetime(year=2023, month=1, day=4, hour=16, minute=59),
            # Thursday 5 January 2023 @ 4pm
            Timestamp(year=2023, month=1, day=5, hour=16),
            # 8am
            datetime.time(hour=11),
            # Friday 6 January 2023
            Timestamp(year=2023, month=1, day=6, hour=10)))
    def test_inside_of_hours(self, value):
        """Test cases that are INSIDE of working hours."""
        actual = is_working_hours(value=value)

        expected = True

        assert actual == expected
