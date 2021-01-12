import sys

N = int(input())

measurements = []

for i in range(N):
    row = list(map(int, input().split()))
    measurements.append(row)

def rotate(measurements):
    new_grid = []

    for i in range(len(measurements)):
        new_row = []
        for j in range(len(measurements)):
            new_row.append(measurements[j][i])
        new_row.reverse()
        new_grid.append(new_row)

    return new_grid

def check_if_ok(measurements):
    for i in range(len(measurements)):
        for j in range(1, len(measurements)):
            if not(measurements[i][j] > measurements[i][j - 1]):
                return False

    for k in range(1, len(measurements)):
        if not(measurements[k][0] > measurements [k - 1][0]):
            return False

    return True

while True:
    if check_if_ok(measurements):
        for row in measurements:
            for item in row:
                print(item, end=" ")
            print()
        sys.exit()
    else:
        measurements = rotate(measurements)
