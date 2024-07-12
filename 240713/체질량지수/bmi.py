arr = input().split()
h = int(arr[0])
w = int(arr[1])

bmi = w * 100 * 100 // (h * h)

# 출력
print(bmi)
if bmi >= 25:
	print("Obesity")