arr = input().split()
a, b = int(arr[0]), int(arr[1])

sum_val = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1

# average
avg = sum_val / cnt

print(f"{sum_val} {avg:.1f}")