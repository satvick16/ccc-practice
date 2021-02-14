#### depth-first search (DFS) ####
print("DFS\n")

graph = {1: [2, 4],
         2: [1, 3, 5],
         3: [2, 5],
         4: [1],
         5: [2, 3]}

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 1)

#### breadth-first search (BFS) ####
print("\nBFS\n")

graph2 = {1: [2, 4],
          2: [1, 3, 5],
          3: [2, 6],
          4: [1],
          5: [2, 6],
          6: [3, 5]}

queue = []
visited2 = [False for i in range(len(graph2))]
distance = [0 for i in range(len(graph2))]

start = 1
visited2[1] = True
distance[start-1] = 0
queue.append(start)

while len(queue) > 0:
    s = queue.pop(0)
    print(s)

    for neighbour in graph2[s]:
        if visited2[neighbour]:
            continue

        visited2[neighbour] = True
        distance[neighbour-1] = distance[s-1] + 1
        queue.append(neighbour)

print(distance)

################# 2D BFS ######################

q = [start]
visited = [[False for i in range(M)] for j in range(N)]
visited[start] = True
distance = [[0 for i in range(M)] for j in range(N)]

distance[start[0]][start[1]] = 0

while len(q) > 0:
    s = q.pop(0)

    for neighbour in graph[tuple(s)]:
        if visited[neighbour[0]][neighbour[1]]:
            continue

        if room[neighbour[0]][neighbour[1]] == ".":
            d = abs(neighbour[0] - s[0] + neighbour[1] - s[1])
            distance[neighbour[0]][neighbour[1]] = distance[s[0]][s[1]] + d
            
        visited[neighbour[0]][neighbour[1]] = True
        q.append([neighbour[0], neighbour[1]])
