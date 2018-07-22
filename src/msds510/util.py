# 4a
import datetime

numbers = "0123456789"


def get_month(input1):
    """The get_month function takes an argument and returns the numerical month."""
    if input1[0] in numbers:
        month_number = datetime.datetime.strptime(input1, '%d-%b').month
        print(month_number)
    else:
        month_number = datetime.datetime.strptime(input1, '%b-%y').month
        return month_number

# b


def get_date_joined(input2, input3):
    """The get_date_joined function takes two arguments, a year, and the month value and returns a date."""
    yearss = int(input2)

    if input3[0] in numbers:
        month_numbers = datetime.datetime.strptime(input3, '%d-%b').month
    else:
        month_numbers = datetime.datetime.strptime(input3, '%b-%y').month

    day = 1

    date1 = datetime.date(yearss, month_numbers, day)
    date2 = datetime.datetime.combine(date1, datetime.time())
    date3 = date2.date()
    return date3

# c


def days_since_joined(input4, input5):
    """The function days_since_joined takes two arguments, a year and month.
    Then it gives the difference of today versus that date and provides it in days."""
    yearss = int(input4)

    if input5[0] in numbers:
        month_numbers = datetime.datetime.strptime(input5, '%d-%b').month
    else:
        month_numbers = datetime.datetime.strptime(input5, '%b-%y').month

    day = 1

    date1 = datetime.date(yearss, month_numbers, day)
    date2 = datetime.datetime.combine(date1, datetime.time())
    date3 = date2.date()
    today = datetime.date.today()

    result1 = abs(today - date3).days
    return result1


if __name__ == "__main__":
    import sys
    # util(int(sys.argv[1]))
    int(sys.argv[1])
