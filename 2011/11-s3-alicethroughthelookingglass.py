T = int(input())

data = []

for i in range(T):
    m, x, y = input().split()
    data.append([int(m), int(x), int(y)])

grid = [[0, 0, 0, 0, 0] for i in range(5)]

grid[1][0] = 1
grid[2][0] = 1
grid[3][0] = 1
grid[2][1] = 1

grid[1][1] = 2
grid[2][2] = 2
grid[3][1] = 2

def search(m, x, y, grid, lim):
    interval = 5 ** m

    if m == lim:
        if grid[][] == 0:
            pass
        elif grid[][] == 1:
            pass
        else:
            pass
    else:            
        if grid[x//interval][y//interval] == 0:
            return "empty"
        elif grid[x//interval][y//interval] == 1:
            return "crystal"
        else:
            return search(m+1, x, y, grid, lim)

for i in data:
    print(search(1, i[1], i[2], grid, i[0]))
