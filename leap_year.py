def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 == 0:
        return True
    else :
        return False

if is_leap_year(2025):
    print(f"{2020} leap year")
else:
    print(f"{2020} not a leap year")
