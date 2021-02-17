'''
adj = {1: [[b, w], [b, w]],
       2: [[b, w]],
       3: []}
'''

start = 1

distance = [9999999 for i in range(N)]
distance[start-1] = 1

q = [] # try collections deque
q.append([0, start])

processed = [False for i in range(N)]

while len(q) > 0:
    a = q[0][1]
    q.pop(0)

    if processed[a-1]:
        continue
    
    processed[a-1] = True

    for u in adj[a]:
        b = u[0]
        w = u[1]

        if distance[a-1]+w < distance[b-1]:
            distance[b-1] = distance[a-1]+w
            q.append([distance[b-1], b])
