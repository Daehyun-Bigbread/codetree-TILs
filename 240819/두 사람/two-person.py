A = input().split()
B = input().split()

a1 = int(A[0]) #나이
a2 = str(A[1]) #성별

b1 = int(B[0]) #나이
b2 = str(B[1]) #성별

if (a1 > 19 or b1 > 19) and (a2 == 'M' or b2 == 'M'):
    print(1)
else:
    print(0)