def is_leap():
    return 1900 <= year <= 10**5 and year % 4 == 0 and \
        (year % 100 != 0 or year % 400 == 0)


year = int(input())
print(is_leap())
