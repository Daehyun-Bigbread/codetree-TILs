a, b = map(int, input().split())

sum_val = 0
for a in range(b):
    if a % b == 5:
        sum_val += 1

print(sum_val)