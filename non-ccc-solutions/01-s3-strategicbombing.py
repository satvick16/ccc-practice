import sys
import copy

roads = []

points = set()

while True:
    road = sys.stdin.readline()

    if road == "**\n":
        break
    else:
        roads.append([road[0], road[1]])
        points.add(road[0])
        points.add(road[1])

graph = {}

for i in points:
    graph[i] = []

for road in roads:
    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0])

dr = []

for road in roads:
    flag = False
    graph_copy = copy.deepcopy(graph)

    graph_copy[road[0]].remove(road[1])
    graph_copy[road[1]].remove(road[0])

    q = []
    visited = {}

    for point in points:
        visited[point] = False

    start = 'A'
    end = 'B'
    visited['A'] = True
    q.append(start)

    while len(q) > 0:
        s = q.pop(0)

        for neighbour in graph_copy[s]:
            if visited[neighbour]:
                continue

            if neighbour == end:
                flag = True
                break

            visited[neighbour] = True
            q.append(neighbour)

    if not flag:
        dr.append(road)

if len(dr) == 0:
    print("There are 0 disconnecting roads.")
else:
    for item in dr:
        print(item[0], end="")
        print(item[1])
    print("There are {} disconnecting roads.".format(len(dr)))
