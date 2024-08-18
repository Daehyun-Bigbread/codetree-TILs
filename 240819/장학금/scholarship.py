arr = input().split()

x = int(arr[0])
y = int(arr[1])

if x >= 90 and y >= 95:
    print(10)
elif x >= 90 and y >= 90:
    print(5)
else:
    print(0)