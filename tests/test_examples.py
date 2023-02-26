"""Examples for testing functionality."""

# Standard library imports
# n/a

# Third party imports

import numpy as np
import pandas as pd
import pytest

# Local application imports
from conftest import Data


@pytest.fixture(scope="session")
def myfibonacci():
    """Create test data."""

    return [1, 1, 2, 3, 5, 8, 13, 21, 34]

@pytest.mark.usefixtures("mydata")
class TestFixtures(Data):
    """Test Fixtures are created as expected."""

    def test_inherited(self, mydata):

        assert isinstance(mydata, pd.DataFrame)

    def test_fibonacci(self, myfibonacci):

        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34]

        actual = myfibonacci

        assert actual == expected


class TestAdditionalAsserts:
    """Test beyond-plain asserts."""

    def test_absolute_tolerance(self):

        expected = [1_000, 5_000]

        actual = [1_001, 4_999]

        assert np.allclose(
            np.array(actual),
            np.array(expected),
            atol=1,
        )

    def test_relative_tolerance(self):

        expected = [1, 100, 10_000]

        actual = [1.01, 99, 10_010]

        assert np.allclose(
            np.array(actual),
            np.array(expected),
            rtol=0.1,
        )

    def test_pandas(self):

        expected = pd.DataFrame({
            "x": [1, 2, 3, 4, 5],
            "y": [10, 20, 30, 40, 50]
        })

        actual = pd.DataFrame({
            "x": [1, 2, 3, 4, 5],
            "y": [10.0, 20.0, 30.0, 40.0, 50.0]
        })

        # Notice that there's no assert!
        pd.testing.assert_frame_equal(
            left=actual,
            right=expected,
            check_dtype=False,
            rtol=0,
            atol=0,
        )

    def test_raises(self):

        def broken():
            raise NotImplementedError("Broken")

        with pytest.raises(NotImplementedError):
            broken()

    @pytest.mark.skip(reason="Test incomplete")
    def test_incomplete(self):

        assert False
