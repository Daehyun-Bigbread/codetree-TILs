arr = input().split()
a, b = int(arr[0]), int(arr[1])

if isinstance(a, int):
    for i in range(1, b+1):
        print(a, end="")
else:
    if a <= 0:
        print(0)