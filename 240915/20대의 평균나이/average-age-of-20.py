age = 0
count = 0

while True:
    n = int(input())
    age += n
    count += 1

    if n < 20 and n >= 30:
        break

avg = age / count

print(f"{avg:.2f}")