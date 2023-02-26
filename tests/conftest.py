"""Configure tests."""

# Standard library imports
import datetime
import os
import sys

# Third party imports
import numpy as np
import pandas as pd
import pytest

# Local application imports
# n/a

# Allow local application imports from superhelpful as if it were a PyPI package
project_path = os.path.join(
    os.path.dirname(__file__),  # /tests
    "..",  # /
)

if project_path not in sys.path:

    sys.path.append(project_path)


class Data:
    """Define example data."""

    @pytest.fixture(scope="class")
    def mydata(self):
        """Define test data at 6-hourly intervals."""
        # Create datetimes at 6-hour intervals (4 per day) for 30 days
        x = [
            datetime.datetime(year=2000, month=1, day=1) +
            datetime.timedelta(hours=6) for x in range(4 * 30)
        ]

        y_base = [10 * i for i in range(len(x))]
        y_noise = [np.random.normal(loc=0, scale=0.3) for _ in range(len(x))]

        y = [b + n for b, n in zip(y_base, y_noise)]

        df = pd.DataFrame.from_dict({
            "datetime": x,
            "value": y,
        })

        df.set_index("datetime", inplace=True)

        return df
