##import sys
##
##N, Q = map(int, sys.stdin.readline().split())
##
##ais = list(map(int, sys.stdin.readline().split()))
##
##queries = [[] for i in range(Q)]
##
##for i in range(Q):
##    queries[i] = list(map(int, sys.stdin.readline().split()))
##
##for q in queries:
##    if q[0] == 1:
##        r = ais.count(q[1])
##
##        for i in range(r):
##            ais.append(q[1] - (q[1] // 2))
##            ais.append(q[1] // 2)
##            ais.remove(q[1])
##    else:
##        print(ais.count(q[1]))

################################################

##import sys
##
##N, Q = map(int, sys.stdin.readline().split())
##
##ais = list(map(int, sys.stdin.readline().split()))
##
##balls = {}
##
##for i in range(max(ais)+1):
##    balls[i] = ais.count(i)
##
##queries = [[] for i in range(Q)]
##
##for i in range(Q):
##    queries[i] = list(map(int, sys.stdin.readline().split()))
##
##for q in queries:
##    if q[0] == 1:
##        r = balls[q[1]]
##        balls[q[1]] = 0
##        
##        balls[q[1] // 2] += r
##        balls[q[1] - (q[1] // 2)] += r
##    else:
##        print(balls[q[1]])

###################################################

import sys

N, Q = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

queries = [[] for i in range(Q)]

for i in range(Q):
    queries[i] = list(map(int, sys.stdin.readline().split()))

