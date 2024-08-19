# 변수 선언 및 입력
inp = input().split()
a1, a2 = inp[0], int(inp[1])
inp = input().split()
b1, b2 = inp[0], int(inp[1])
inp = input().split()
c1, c2 = inp[0], int(inp[1])


if a1 == 'Y' and a2 >= 37: # 첫번쨰 A
    if (b1 == 'Y' and b2 >= 37) or (c1 == 'Y' and c2 >= 37):
        print("E")
    else:
        print("N")
else:
    if (b1 == 'Y' and b2 >= 37) and (c1 == 'Y' and c2 >= 37):
        print("E")
    else:
        print("N")