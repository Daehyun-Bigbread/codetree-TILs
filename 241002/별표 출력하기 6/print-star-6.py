n = int(input())

for i in range(n): 
    for _ in range(i): # n개의 줄동안 공백 i는 1씩 증가
        print(" ", end=" ")
    for _ in range((2 * n) - (2 * i) - 1): # n개의 줄동안 별의 개수는 (2 * n) - (2 * i) - 1
        print("*", end=" ")
    print()

for i in range(n-2, -1, -1):
    for _ in range(i): # n-1개의 줄 동안 공백의 개수는 n -i -2, 각 줄마다 1개씩 감소
        print(" ", end=" ")
    for _ in range((2 * n) - (2 * i) - 1): # n-1개의 줄 동안 별의 개수는 3 + (2 * i)
        print("*", end=" ")
    print()