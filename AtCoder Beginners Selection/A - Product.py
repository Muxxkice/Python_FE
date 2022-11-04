l = input()
x,y = list(map(int, l.split()))
product = x * y

if product % 2 == 0:
    print("Even")
else:
    print("Odd")
