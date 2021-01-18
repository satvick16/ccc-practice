import sys

N = int(sys.stdin.readline())

b = []

for i in range(N):
    options = list(map(int, input().split()))
    b.append(options)

book = {}

for i in range(len(b)):
    book[i+1] = b[i][1:]

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
        

        visited.append(neighbour)
        distance[neighbour-1] = distance[s-1] + 1
        queue.append(neighbour)

print(distance)
