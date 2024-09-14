n = int(input())
count = 0 # 나눗셈 진행 횟수
div = n # 몫 저장

for i in range(1, n+1):
    div = div // i # 반복문 반복 횟수만큼 나누기, 나눈 후 몫 저장
    count += 1 # 나누기 할때 마다 count 횟수 +1

    if div <= 1: # 만약 몫이 1보다 작거나 같으면? 멈추기
        break
    else:
        continue

print(count) # 횟수 출력