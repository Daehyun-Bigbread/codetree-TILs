arr = input().split()
a, b = int(arr[0]), int(arr[1])

print(f"{a//b}.", end="")

a %= b

for _ in range(20):
    # 나머지에 10 곱한 값을 기준으로
    # b로 나누었을 떄의 몫을 구해줍니다.
    a *= 10
    print(a // b, end="")

    # a를 b로 나눈 나머지를 게속 갱신해줍니다.
    a %= b