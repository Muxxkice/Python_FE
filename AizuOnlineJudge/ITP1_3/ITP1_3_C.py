while True:
    l = input()
    x,y = list(map(int, l.split()))
    if x == 0 and y == 0:
        break
    elif x > y:
        x, y = y,x
    print(x,y)
