while True:
    l = input()
    m,f,r = list(map(int, l.split()))
    sum = m + f
    if m == -1 & f == -1 & r == -1 :
        break
    elif (m == -1) | (f == -1):
        print("F")
    elif sum >= 80:
        print("A")
    elif 65 <= sum < 80:
        print("B")
    elif 50 <= sum < 65:
        print("C")
    elif 30 <= sum < 50:
        if 50 <= r:
            print("C")
        else:
            print("D")
    else:
        print("F")
