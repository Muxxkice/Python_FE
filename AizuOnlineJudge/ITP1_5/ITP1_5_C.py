while True:
    l = input()
    h,w = list(map(int, l.split()))
    if h == 0 & w == 0:
        break
    else:
        for i in range(h):
            for j in range(w):
                if i % 2 == 0:
                    if j % 2 == 0:
                        print("#", end="")
                    else:
                        print(".", end="")
                else:
                    if j % 2 == 0:
                        print(".", end="")
                    else:
                        print("#", end="")
            print()
        print()
