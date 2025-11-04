#Program to check whether given year is leap year or not.

year = int(input("Enter a year: "))

# Leap year conditions:
# 1. Divisible by 4, but not by 100
# 2. OR divisible by 400

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")