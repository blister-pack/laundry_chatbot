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


# this function returns what day of the week is today
def today():
    day_today = datetime.now().weekday()
    return weekdays[day_today]


def tomorrow():
    day_tomorrow = datetime.now().weekday() + 1
    return weekdays[day_tomorrow]


# this function returns the third friday of the month
def get_third_friday(year, month):
    first_day_of_the_month = datetime(year, month, 1)
    days_until_friday = (4 - first_day_of_the_month.weekday() + 7) % 7
    first_friday = first_day_of_the_month + timedelta(days=days_until_friday)
    third_friday = first_friday + timedelta(days=14)
    return third_friday


def get_all_third_fridays():
    current_year = datetime.now().year

    for month in range(1, 13):
        """we use formatted date to remove the timestamp"""
        third_friday = get_third_friday(current_year, month)
        formatted_date = third_friday.strftime("%Y-%m-%d")
        all_third_fridays[f"{month_mapping[month]}"] = f"{formatted_date}"

    return all_third_fridays


def is_right_week(month_to_check=datetime.now().month, current_day=datetime.now().day):
    this_month = month_mapping[month_to_check]
    # title because data is saved with a capitalized month
    # only need 2 last chars because it's the day (2024-02-16)
    # gotta turn it into an int so I can do math with it
    sixth_friday_of_the_month = int(all_third_fridays[this_month.title()][-2::])

    """if the difference between the now and the third friday of
    the month is 4 then it is monday of the same week, if it's 0
    then it is friday!"""
    if 0 <= sixth_friday_of_the_month - current_day <= 4:
        return True
    return False



if __name__ == "__main__":
    print(today())
    print(tomorrow())
    print(get_third_friday(2024, 11))
    print(get_all_third_fridays())
    print(all_third_fridays["January"])
    print(int(all_third_fridays["january".title()][-2::]))
    print(is_right_week(1, 14))
