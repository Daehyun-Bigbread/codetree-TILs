satisfied = True

while True:
    n = int(input())
    if n % 3 == 0:
        satisfied = False
    break

if satisfied == False:
    print(1)
else:
    print(0)