A = input().split()
B = input().split()

a1 = int(A[0]) #수학
a2 = int(A[1]) #영어

b1 = int(B[0]) #수학
b2 = int(B[1]) #영어

if a1 > b1:
    print("A")
elif a1 == b1 and a2 > b2:
    print("A")
else:
    print("B")