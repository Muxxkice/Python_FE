def junkan(num):
    m = 1
    p = 1
    s = 0
    t = 0
    while True:
        m = (m * 10) % n
        p = (((p * 10) % n) * 10) % n
        print(f"m:{m},p:{p}")
        if (m == p):
            break
    if (p != 0):
        p = 1
        s = 1
        while m != p:
            s += 1
            m = (m * 10) % n
            p = (p * 10) % n
            print(f"s:{s} m:{m} p:{p}")
        p = (p * 10) % n
        t = s
        while m != p:
            t += 1
            p = (p * 10) % n
            print(f"t:{t} p:{p}")

        print(s,t)

n = int(input())
junkan(n)
