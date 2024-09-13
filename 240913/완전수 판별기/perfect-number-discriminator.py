n = int(input())
sum_val = 0

# n(입력값)을 i(반복횟수)로 나머지 판별 - 완전수
for i in range(1, n):
    if n % i == 0:
        sum_val += i

if sum_val == n:
    print("P")
else:
    print("N")