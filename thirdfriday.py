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
# this function returns the third friday of the month
def get_third_friday(year, month):
    first_day = datetime(year, month, 1)
    days_until_friday = (4 - first_day.weekday() + 7) % 7
    first_friday = first_day + timedelta(days=days_until_friday)
    third_friday = first_friday + timedelta(days=14)
    return third_friday

# this function returns what day of the week is today
def today():
    day_today = datetime.now().weekday()
    return weekdays[day_today]

def tomorrow():
    day_tomorrow = datetime.now().weekday() + 1
    return weekdays[day_tomorrow]

if __name__ == "__main__":
    print(today())
    print(tomorrow())
