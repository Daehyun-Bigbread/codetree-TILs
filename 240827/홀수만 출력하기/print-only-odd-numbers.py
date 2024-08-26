N = int(input())

for i in range(1, N+1):
    num = int(input())

    if num % 3 == 0 and num % 2 == 1:
        print(num)