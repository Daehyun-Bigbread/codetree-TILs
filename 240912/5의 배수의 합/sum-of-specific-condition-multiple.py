a, b = map(int, input().split())

sum_val = 0
for i in range(a, b):
    if i % 5 == 0:
        sum_val += 1

print(sum_val)