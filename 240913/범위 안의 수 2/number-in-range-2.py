sum_val = 0
count = 0

for _ in range(10):
    num = int(input())

    if num >= 0 and num <= 200:
        sum_val += num
        count += 1

avg = sum_val / count
print(f"{sum_val} {avg:.1f}")