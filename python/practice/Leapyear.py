"""A leap year is a year:
    -If a year is divisible by 4, it is a leap year.
    -However, if that year is also divisible by 100, it is not a leap year, unless...
    -The year is divisible by 400, in which case it is a leap year.
    """


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
