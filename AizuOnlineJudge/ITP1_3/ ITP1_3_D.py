l = input()
a,b,c = list(map(int, l.split()))
ans = 0
while True:
    if a > b:
        break
    elif c % a == 0 :
        ans += 1
    a += 1

print(ans)
