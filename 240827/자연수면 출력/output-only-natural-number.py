arr = input().split()
a, b = int(arr[0]), int(arr[1])

if isinstance(a, int):
    if a <= 0:
        print(0)
    else:
        for i in range(1, b+1):
            print(a, end="")