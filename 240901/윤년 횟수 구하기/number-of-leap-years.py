n = int(input())

cnt = 0

for i in range (1, n+1):
    # 4로 나누어 떨어지면서 100으로 나누어 떨어지지 않는 수, 400의 배수
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        cnt += 1

print(cnt)