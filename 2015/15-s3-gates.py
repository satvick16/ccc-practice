import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

gates = [i for i in range(1, G+1)]
planes = [0 for i in range(P)]

for i in range(P):
    planes[i] = int(sys.stdin.readline())

counter = 0

for i in planes:
    flag = False
    for j in range(i, 0, -1):
        if j in gates:
            counter += 1
            gates.remove(j)
            flag = True
            break
    if flag:
        pass
    else:
        break

print(counter)
