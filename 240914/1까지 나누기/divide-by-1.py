n = int(input())
count = 0
div = n

for i in range(1, n+1):
    div = div // i
    count += 1

    if div <= 1:
        break
    else:
        continue

print(count)