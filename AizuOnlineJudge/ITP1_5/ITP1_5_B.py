while True:
    l = input()
    h,w = list(map(int, l.split()))
    if h == 0 & w == 0:
        break
    else:
        for i in range(h):
            for j in range(w):
                if (i == 0) | (i == h-1) | (j == 0) |(j == w-1):
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()
