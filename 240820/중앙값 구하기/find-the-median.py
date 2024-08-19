arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if a > b:
    if a > c:
        print(c)
    else:
        print(a)
else:
    if b > c:
        print(c)
    else:
        print(b)