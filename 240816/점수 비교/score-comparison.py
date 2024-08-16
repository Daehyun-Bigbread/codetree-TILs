# 변수 선언, 입력
inp = input()
arr = inp.split()
a_math = int(arr[0])
a_eng = int(arr[1])

inp = input()
arr = inp.split()
b_math = int(arr[0])
b_eng = int(arr[1])

# 출력
if a_math > b_math and a_eng > b_eng:
	print(1)
else:
	print(0)