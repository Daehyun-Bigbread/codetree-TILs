arr1 = input().split()
arr2 = input().split()

A1 = int(arr1[0])
A2 = int(arr1[0])

B1 = int(arr2[0])
B2 = int(arr2[1])

if A1 > B1 and B1 > B2:
    print(1)
else:
    print(0)