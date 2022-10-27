l = input()
a,b = list(map(int, l.split()))

print(int(a/b),a%b ,"{:.5f}".format(a/b))
