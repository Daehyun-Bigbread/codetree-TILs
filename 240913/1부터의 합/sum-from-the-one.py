n = int(input())
count = 0

for i in range(1, 101):
    count += i
    if count >= n:
        print(i)
        break