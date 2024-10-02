n = int(input())

for i in range(n): # i는 현재 줄의 index (0~n-1까지 반복)
    for _ in range(n-i-1): # n개의 줄동안 공백의 개수는 n-1개 에서 각 줄마다 1개씩 감소
        print(" ", end=" ") #
    for _ in range(i+1): # n개의 줄동안 특정 문자의 개수가 줄어드는 부분 출력
        print("@", end=" ") # @ 기호를 오른쪽으로 정렬
    print() # 줄 전환

for i in range(n-2, -1, -1): # i는 n-2에서 0까지 역순으로 반복
    for _ in range(i+1):
        print("@", end=" ")
    print()