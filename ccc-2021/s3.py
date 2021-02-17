import sys
import math

N = int(sys.stdin.readline())

friends = [[] for i in range(N)]

for i in range(N):
    p, w, d = map(int, sys.stdin.readline().split())
    friends[i] = [p, w, d]

if len(friends) == 1:
    c = friends[0][0]
    print(c)
    sys.exit()
else:
    num = 0
    den = 0

    for friend in friends:
        num += friend[0] * friend[1]
        den += friend[1]

    c = math.floor(num / den)

t = 0

for friend in friends:
    if abs(friend[0] - c) <= friend[2]:
        continue
    
    t += (abs(c - friend[0]) - friend[2]) * friend[1]

print(t)
