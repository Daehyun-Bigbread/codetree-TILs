arr = input().split()
a, b = int(arr[0]), int(arr[1])

for i in range (a, b, 2):
    print(a * i, end=" ")