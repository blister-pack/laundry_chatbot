import datetime
import pytest
from source.business_logic import today
import unittest.mock as mock


@pytest.fixture
def year_to_check():
    return 2023


@pytest.mark.parametrize(
    "month_to_check, day_to_check, expected_result",
    [
        (1, 3, "tuesday"),
        (1, 18, "wednesday"),
        (2, 3, "friday"),
        (2, 17, "friday"),
        (3, 3, "friday"),
        (3, 13, "monday"),
        (4, 5, "wednesday"),
        (4, 19, "wednesday"),
        (4, 21, "friday"),
    ],
)
@mock.patch("source.business_logic.datetime")
def test_get_today(
    mock_datetime,
    year_to_check,
    month_to_check,
    day_to_check,
    expected_result,
):
    mock_datetime.now.return_value = datetime.datetime(
        year_to_check, month_to_check, day_to_check
    )

    assert today() == expected_result
