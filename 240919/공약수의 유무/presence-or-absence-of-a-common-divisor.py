a, b = map(int, input().split())
satisfied = False

for i in range(a, b+1):
    if a % i == 0 and b % i == 0:
        satisfied = True

if satisfied == True:
    print(1)
else:
    print(0)