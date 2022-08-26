def decode(days):
    years, days_ = divmod(days, 365)
    months, days_ = divmod(days, 30)
    weeks, days_ = divmod(days, 7)
    return years, months, weeks, days_


print(decode(365))
