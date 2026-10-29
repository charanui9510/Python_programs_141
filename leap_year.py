### Checking whether the given year is a leap year or not

# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 ==0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else :
#         return False
#
# if is_leap_year(2025):
#     print(f"{2020} leap year")
# else:
#     print(f"{2020} not a leap year")


### Printing the leap years in the given range

leap_year = True
counter = 0
for i in range(2000,2026) :
    if i % 4 == 0 and i % 100 != 0 :
        counter = counter + 1
        print(i)

print(f" the total number of leap years in the given range are {counter} ")
