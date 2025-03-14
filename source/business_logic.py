from calendar import month
from datetime import datetime, timedelta

weekdays = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

month_mapping = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
all_third_fridays = {"month": "day"}


def today(year=None, month=None, day=None):
    if day == None:
        day = datetime.now().weekday()
    return weekdays[day]


def tomorrow():
    day_tomorrow = datetime.now().weekday() + 1
    return weekdays[day_tomorrow]


# this function returns the third friday of the month
def get_third_friday(year, month):
    first_day_of_the_month = datetime(year, month, 1)
    days_until_friday = (4 - first_day_of_the_month.weekday() + 7) % 7
    first_friday = first_day_of_the_month + timedelta(days=days_until_friday)
    third_friday = first_friday + timedelta(days=14)
    return third_friday.strftime("%Y-%m-%d")


def get_all_third_fridays(year_to_check=datetime.now().year):

    for month in range(1, 13):
        """we use formatted date to remove the timestamp"""
        third_friday = get_third_friday(year_to_check, month)
        all_third_fridays[f"{month_mapping[month]}"] = f"{third_friday}"

    return all_third_fridays


def is_right_week(
    year_to_check=None,
    month_to_check=None,
    day_to_check=None,
):
    """
    Determines if the given date falls within the same week as the third Friday of the month.

    This function checks if the provided day is within the range of Monday to Friday
    of the same week as the third Friday of the specified month. If no date is provided,
    it defaults to the current date.

    Parameters:
    ----------
    year_to_check : int, optional
        The year to check (defaults to the current year).
    month_to_check : int, optional
        The month to check (defaults to the current month).
    day_to_check : int, optional
        The day to check (defaults to the current day).

    Returns:
    -------
    bool
        True if the given date is within Monday-Friday of the third Friday's week, False otherwise.

    Notes:
    ------
    The default arguments are set to `None` and assigned inside the function to avoid caching issues.
    If we had used `datetime.now().year` as a default argument directly, it would only be evaluated once
    when the function is first loaded, rather than updating each time the function is called.
    """
    if year_to_check == None:
        year_to_check = datetime.now().year
    if month_to_check == None:
        month_to_check = datetime.now().month
    if day_to_check == None:
        day_to_check = datetime.now().day

    third_friday_month = get_third_friday(year_to_check, month_to_check).split("-")[2]

    """if the difference between the now and the third friday of
    the month is 4 then it is monday of the same week, if it's 0
    then it is friday!"""
    if 0 <= int(third_friday_month) - day_to_check <= 4:
        return True
    return False


if __name__ == "__main__":
    print(today())
    print(tomorrow())
    print(get_third_friday(2024, 11))
    print(get_all_third_fridays())
    print(all_third_fridays["January"])
    print(int(all_third_fridays["january".title()][-2::]))
    print(is_right_week(2025, 1, 14))
