arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a == 0:
    if b <= 19:
        print("Boy")
    else:
        print("Man")
else:
    if b <= 19:
        print("Girl")
    else:
        print("Woman")