n = int(input())

if n % 2 == 1 and n <= 7:
    print(31)
elif n % 2 == 0:
    if n == 2:
        print(28)
    elif n >= 8 and n <= 12:
        print(30)
    else:
        print(31)