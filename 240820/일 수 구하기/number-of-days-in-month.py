n = int(input())

if n % 2 == 1 and n <= 7:
    print(31)
elif n % 2 == 0 and n >= 8:
    print(31)
elif n == 2:
    print(28)
else:
    print(30)