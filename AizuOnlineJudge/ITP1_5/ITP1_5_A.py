while True:
    l = input()
    h,w = list(map(int, l.split()))
    if h == 0 & w == 0:
        break
    else:
        for i in range(h):
            for j in range(w):
                    print("#", end="")
            print()
        print()
