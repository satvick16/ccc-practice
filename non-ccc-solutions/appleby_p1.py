T = int(input())

tris = [[] for i in range(T)]

for i in range(T):
    x = list(map(int, input().split()))
    x.sort()
    tris[i] = x

for tri in tris:
    x = (tri[0] ** 2 + tri[1] ** 2) ** 0.5

    if x == tri[2]:
        print("R")
    elif x < tri[2]:
        print("O")
    else:
        print("A")
