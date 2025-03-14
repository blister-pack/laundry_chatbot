import pytest
from source.business_logic import is_right_week
import datetime


@pytest.fixture
def year_to_check():
    return 2023


@pytest.mark.parametrize(
    "month_to_check, day_to_check, expected_result",
    [
        (1, 3, False),
        (1, 18, True),
        (2, 3, False),
        (2, 17, True),
        (3, 3, False),
        (3, 13, True),
        (4, 5, False),
        (4, 19, True),
        (4, 21, True),
    ],
)
def test_return_is_right_week(
    year_to_check,
    month_to_check,
    day_to_check,
    expected_result,
):
    assert is_right_week(year_to_check, month_to_check, day_to_check) == expected_result
