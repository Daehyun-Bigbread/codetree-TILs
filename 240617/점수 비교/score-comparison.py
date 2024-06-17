a = input()
b = input()

arr1 = a.split()
a1 = int(arr1[0])
a2 = int(arr1[1])

arr2 = b.split()
b1 = int(arr2[0])
b2 = int(arr2[1])

if a1 > b1 and a2 > b2:
    print(1)
else:
    print(0)