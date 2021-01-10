grid = [1, 2, 3, 4]

seq = input()
sequence = [i for i in seq]

def hflip(grid):
    return [grid[2], grid[3], grid[0], grid[1]]

def vflip(grid):
    return [grid[1], grid[0], grid[3], grid[2]]

for i in sequence:
    if i == "H":
        grid = hflip(grid)
    else:
        grid = vflip(grid)

print(grid[0], grid[1])
print(grid[2], grid[3])
