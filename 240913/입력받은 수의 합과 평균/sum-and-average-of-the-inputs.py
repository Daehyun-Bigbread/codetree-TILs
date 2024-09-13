n = int(input())

sum_val = 0

for i in range(n):
    num = int(input())
    sum_val += num

avg = sum_val / n
print(f"{sum_val} {avg:.1f}")