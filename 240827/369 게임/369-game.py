n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print("0", end=" ")
    elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9: # 10으로 나누었을때 나머지가 3,6,9 (한자리 수)
        print("0", end=" ")
    elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9: # 10으로 나누었을때 몫이 3,6,9
        print("0", end=" ")
    else:
        print(i, end=" ")