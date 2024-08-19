arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if a > b :
    if c > a: # c > a > b
        print(a)
    elif b > c: # a > b > c 
        print(b)
    else:  # a > c > b 
        print(c)  
else:
    # a < b 
    if c < a: # c < a < b
        print(a) 
    elif b < c: # a < b < c 
        print(b)
    else: # a < c < b
        print(c)