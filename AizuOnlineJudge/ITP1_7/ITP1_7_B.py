ans = 0
while True:
    l = input()
    n,x = list(map(int, l.split()))
    if n == 0 & x == 0:
        break
    else:
        for i in range(1,n+1):
            for j in range(i+1,n):
                for k in range(j+1,n+1):
                    sum = i + j + k
                    if sum == x:
                        ans += 1

    print(ans)
