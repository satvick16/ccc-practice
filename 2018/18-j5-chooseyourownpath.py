N = int(input())

adj = {}

for i in range(1, N+1):
    adj[i] = []
    page = list(input().split())

    for j in page[1:]:
        adj[i].append([int(j), 1])

start = 1

distance = [9999999 for i in range(N)]
distance[start-1] = 1

q = []
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

if False in processed:
    print("N")
else:
    print("Y")

candidates = []

for i in range(len(distance)):
    if len(adj[i+1]) == 0:
        candidates.append(distance[i])

print(min(candidates))
