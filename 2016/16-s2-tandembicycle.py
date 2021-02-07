q = int(input())
N = int(input())

dmoj = list(map(int, input().split()))
peg = list(map(int, input().split()))

if q == 1:
    dmoj.sort()
    peg.sort()

    speed = 0
    
    for i in range(N):
        speed += max(dmoj[i], peg[i])
else:
    dmoj.sort()
    peg.sort()
    peg.reverse()

    speed = 0
    
    for i in range(N):
        speed += max(dmoj[i], peg[i])

print(speed)
