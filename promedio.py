a = 0
b = 0
for x in range(0, 50090900):
    a=int(input("numero"))
    b=int(input("numero"))
    if a > 0 and b > 0:
        print((a + b))
        a += 1
        b += 1
    else:
        if a > 0 and b > 0:
            print((a + b) / 2)
            a += 1
            b += 1