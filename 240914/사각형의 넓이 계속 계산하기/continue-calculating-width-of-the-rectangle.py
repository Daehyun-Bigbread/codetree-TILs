while True:
    arr = input().split()
    x, y, t = int(arr[0]), int(arr[1]), str(arr[2])
    print(f"{x*y}")
    
    if t == "C":
        break