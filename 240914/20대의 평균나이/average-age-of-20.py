age = 0
count = 0

while True:
    n = int(input())

    if n >= 30 and n < 20:
        break
    age += n
    count += 1
    
avg = age / count
print(f"{avg:.2f}")