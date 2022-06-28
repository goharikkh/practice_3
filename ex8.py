def month_days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if year % 4 == 0:
            return 29
        return 28
    return 30


print(month_days(3, 2000))
