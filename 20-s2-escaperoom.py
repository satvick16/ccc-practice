M = int(input())
N = int(input())

room = []

for i in range(M):
    row = list(map(int, input().split()))
    room.append(row)

location = [1, 1]
path = []
visited = []

# backtracking
def solve(location, path, visited):
    if location[0] == M and location[1] == N:
        return True

    visited.append(location)

    val = room[location[0] - 1][location[1] - 1]

    factors = []

    for num in range(1, int(val) + 1):
        if val % num == 0:
            factors.append([num, int(val / num)])

    for pair in factors:
        if pair[0] <= M and pair[1] <= N and not([pair[0], pair[1]] in visited):
            if solve([pair[0], pair[1]], path, visited):
                    path.append(location)
                    return True
    return False

if solve(location, path, visited):
    print("yes")
else:
    print("no")
