from datetime import datetime

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
