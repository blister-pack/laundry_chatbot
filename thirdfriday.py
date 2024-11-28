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


# this function returns what day of the week is today
def today():
    day_today = datetime.now().weekday()
    return weekdays[day_today]


def tomorrow():
    day_tomorrow = datetime.now().weekday() + 1
    return weekdays[day_tomorrow]


# this function returns the third friday of the month
def get_third_friday(year, month):
    first_day = datetime(year, month, 1)
    days_until_friday = (4 - first_day.weekday() + 7) % 7
    first_friday = first_day + timedelta(days=days_until_friday)
    third_friday = first_friday + timedelta(days=14)
    return third_friday


def get_all_third_fridays():
    all_third_fridays = [{"month": "day"}]
    current_year = datetime.now().year

    for month in range(1, 13):
        third_friday = get_third_friday(current_year, month)
        all_third_fridays.append({f"{month_mapping[month]}": f"{third_friday}"})

    return all_third_fridays


if __name__ == "__main__":
    print(today())
    print(tomorrow())
    print(get_third_friday(2024, 11))
    print(get_all_third_fridays())
