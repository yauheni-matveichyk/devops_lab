import re
line = str(input('Give me any math problem:'))


def t(line):
    mo = re.fullmatch(r'(?P<n1>-?\d+)(?P<oper>[-/\*\+])(?P<n2>-?\d+)=(?P<n3>-?\d+)',
                      line)
    return mo


mo = t(line)
if not mo:
    print("Error! Bad syntax.")
else:
    if len(line) <= 100 and mo:
        n1 = int(mo.groupdict()['n1'])
        n2 = int(mo.groupdict()['n2'])
        n3 = int(mo.groupdict()['n3'])
        if max(n1, n2, n3) < 30000 and min(n1, n2, n3) > -30000:
            oper = mo.groupdict()['oper']
            if oper == "/" and n2 == 0:
                result = "NO"
            else:
                def m(x, y):
                    return x * y

                def d(x, y):
                    return x / y

                def s(x, y):
                    return x + y

                def _(x, y):
                    return x - y
                do = {"*": m, "/": d, "+": s, "-": _}
                result = "You're right" if n3 == do[oper](
                    n1, n2) else "Incorrect solution"
            print(result)
t(line)
