"""Useful utility functions."""

# Standard library imports
import datetime

# Third party imports
from pandas import Timestamp

# Local application imports
# n/a


def is_working_hours(
    value: datetime.datetime | datetime.time | Timestamp,
    start_time: datetime.time = datetime.time(hour=9),
    end_time: datetime.time = datetime.time(hour=17),
    days_closed: list[str] = ["Saturday", "Sunday"],
) -> bool:
    """Determine if a value is within working hours.

    Args:
        value (Union[datetime.datetime, datetime.time, Timestamp]): Input
            date-time or time to.
        start_time (datetime.time): Start-time of working hours.
        end_time (datetime.time): End-time of working hours.
        days_closed (List[str]): Non-working days. Defaults to ["Saturday",
            "Sunday"].

    Raises:
        TypeError: If value is of the incorrect type.
        ValueError: If days_closed not recognised

    Returns:
        bool: True if value in working hours, False if not in working hours.
    """
    if not isinstance(value, (datetime.time, datetime.datetime, Timestamp)):
        raise TypeError(
            "value must be datetime.time, datetime.datetime, or pd.Timestamp")

    # Lists of recognised days
    known_days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"
        ]

    # Check that the days provided are known
    unknown_days = [x for x in days_closed if x.title() not in known_days]

    if len(unknown_days) > 0:

        raise ValueError(f"Days: {' '.join(unknown_days)}, not recognised.")

    # Convert pd.Timestamp to datetime.datetime
    if isinstance(value, Timestamp):

        value = value.to_pydatetime()

    # Convert datetimes to time
    if isinstance(value, datetime.datetime):

        # Check if day is not a working day
        if value.strftime("%A") in [x.title() for x in days_closed]:

            return False

        # Convert datetime.datetime to datetime.time
        value = value.time()

    # Check if time is before the start of working hours, or after the end of
    # working hours
    if value < start_time or value >= end_time:

        return False

    return True
