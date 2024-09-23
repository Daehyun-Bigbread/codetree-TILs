n = int(input())

for i in range(n):
    for _ in range(n - i):
        print("*", end=" ")
    print()

for j in range(1, n):
    for _ in range(j + 1):
        print("*", end=" ")
    print()