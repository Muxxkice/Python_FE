n = int(input())-1
list = list(map(int, input().split()))
reverse_list = sorted(list, reverse=True)

for i, elem in enumerate(reverse_list):
    if i == n:
        print(elem,end="")
    else:
        print(elem, end=" ")
