a, b = map(int, input().split())

sum_val = 0

if a <= b: # b가 a보다 큰 경우
    for i in range(a, b+1):
        if i % 5 == 0:
            sum_val += i
else:
    for i in range(b, a+1):
        if i % 5 == 0:
            sum_val += i

print(sum_val)