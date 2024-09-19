a, b, c = map(int, input().split())
satisfied = False

for i in range(a, b+1):
    if i % a != 0 and i % b != 0:
        satisfied = True
    
if satisfied == True:
    print("YES")
else:
    print("NO")