x = input()
arr = x.split()
b = int(arr[0])
a = int(arr[1])

result = []

for i in range(b, a - 1, -1):
    if i % 2 != 0:
        result.append(i)

print(" ".join(map(str, result)))