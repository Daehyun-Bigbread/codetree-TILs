arr = input().split()

x = int(arr[0])
y = int(arr[1])

if x >= 90 and y >= 95:
    print(100000)
elif x >= 90 and y >= 90:
    print(50000)
else:
    print(0)