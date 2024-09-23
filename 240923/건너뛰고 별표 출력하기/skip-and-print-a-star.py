n = int(input())

# 증가하는 별 출력
for i in range(1, n + 1):
    print("*" * i)
    print()  # 빈 줄 추가

# 감소하는 별 출력
for j in range(n - 1, 0, -1):
    print("*" * j)
    print()  # 빈 줄 추가