x = input()
arr = x.split()

a = int(arr[0])
b = int(arr[1])

if a > b:
    print(f"{a*b}")
else:
    print(f"{a%b}")