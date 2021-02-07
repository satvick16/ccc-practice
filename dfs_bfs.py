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
visited2 = []
distance = [0 for i in range(len(graph2))]

start = 1
visited2.append(1)
distance[start-1] = 0
queue.append(start)

while len(queue) > 0:
    s = queue.pop(0)
    print(s)

    for neighbour in graph2[s]:
        if neighbour in visited2:
            continue

        visited2.append(neighbour)
        distance[neighbour-1] = distance[s-1] + 1
        queue.append(neighbour)

print(distance)
