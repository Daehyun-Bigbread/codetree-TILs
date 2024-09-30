n = int(input())

for i in range(n): # 세로
    for j in range(n - i, 1, -1): # 공백 출력
        print(" ", end=" ")
    for j in range((2 * i) + 1):
        print("*", end=" ") # 별 출력
    print()