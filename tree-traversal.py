def dfs_tree(graph, node, target):
    if node == target:
        return True

    for neighbour in graph[node]:
        return dfs_tree(graph, neighbour, target)

    return

def bfs(graph, start, target, N):
    q = []
    visited = []

    visited.append(start)
    q.append(start)

    while len(q) > 0:
        s = q.pop(0)

        for child in graph[s]:
            if child == target:
                return True
            
            if child in visited:
                continue

            visited.append(child)
            q.append(child)

    return False
