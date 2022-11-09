N = 6
m = 8
start = [0,1,2,3,4,2,5,4,6]
end = [0,2,3,4,1,5,4,6,2]
edgefirst = [0,1,2,3,4,6,8]
edgenext = [0,0,5,0,7,0,0,0,0]
searched = [0,0,0,0,0,0,0,0,0]
path = [0,0,0,0,0,0,0,0,0]
current = []

for i in range(N +1):
    current.append(edgefirst[i])

top = 1
last = m
x = 1

while last >= 1:
    if (current[x] != 0):
        print(f"current[x]:{current[x]}")
        temp  = current[x]
        searched[top] = temp
        current[x] = edgenext[temp]
        x = end[temp]
        top += 1
        print(f"current:{current}")
        print(f"searched:{searched}")
        print(f"top:{top} last:{last}")
    else:
        print(f"current[x]:{current[x]}")
        top -= 1
        temp = searched[top]
        path[last] = temp
        x = start[temp]
        last -=1
        print(f"searched:{searched}")
        print(f"top:{top} last:{last}")

