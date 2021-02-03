import math

N = int(input())

book = {}

for i in range(1, N+1):
    book[i] = []
    page = list(input().split())

    for j in page[1:]:
        book[i].append(int(j))

queue = []
visited = []
distance = [0 for i in range(N)]

start = 1
visited.append(1)
distance[start-1] = 0
queue.append(start)

while len(queue) > 0:
    s = queue.pop(0)

    for neighbour in book[s]:
        if neighbour in visited:
            continue

        visited.append(neighbour)
        distance[neighbour-1] = distance[s-1] + 1
        queue.append(neighbour)

visited.sort()

if visited == [i for i in range(1, N+1)]:
    print("Y")
else:
    print("N")

##start = 1
##
##distance = [math.inf for i in range(N)]
##distance[start-1] = 0
##
##q = []
##q.append([0, start])
##
##visited = [False for i in range(N)]
##visited[start-1] = True
##
##while len(q) > 0:
##    a = q[0][1]
##    q.pop(0)
##
##    if visited[a]:
##        continue
##
##    visited[a] = True
##
##    for neighbour in book[a]:
##        if distance[a-1]+1 < distance[b-1]:
##            distance[b-1] = distance[a-1] + 1
##            q.append([-1 * distance[b-1], b])
##
##print(distance)

candidates = []

for i in range(len(distance)):
    if len(book[i+1]) == 0:
        candidates.append(distance[i])

print(min(candidates)+1)
