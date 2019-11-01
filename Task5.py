num = int(input("Enter numb: "))


def bswitch(num):
    c = 1

    while num * 2 > c:
        num = num ^ c
        c = c << 1

    print(num)


bswitch(num)
