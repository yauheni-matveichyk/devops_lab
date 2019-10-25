a = int(input("Enter number :"))
sum = str()


def delit(a, b):
    c = a / b
    d = a % b
    return (c, d)


if a == 0:
    sum += "1"
    print(sum)

elif 0 < a < 10:
    sum += str(a)
    print(sum)

else:
    ost = a
    i = 2
    while ost >= 10 and i > 1:
        for i in range(9, 0, -1):
            k, ex = delit(ost, i)
            if ex == 0:
                ost = int(k)
                sum += str(i)
                break

        if i > 1 and ost < 10:
            sum += str(ost)

    if sum == "1":
        print(-1)
    else:
        print(sum[::-1])
