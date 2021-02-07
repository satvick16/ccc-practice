a, b, c = input().split()
d, e, f = input().split()
g, h, i = input().split()

vals = [[a, b, c],
        [d, e, f],
        [g, h, i]]

for row in vals:    
    numxs = row.count("X")

    if numxs == 1:
        if row[0] == "X":
            row[0] = int(row[1]) - (int(row[2]) - int(row[1]))
        elif row[1] == "X":
            row[1] = (int(row[0]) + int(row[2])) / 2
        else:
            row[2] = int(row[1]) - int(row[0]) + int(row[1])

reorg_vals = [[vals[0][0], vals[1][0], vals[2][0]],
              [vals[0][1], vals[1][1], vals[2][1]],
              [vals[0][2], vals[1][2], vals[2][2]]]

for row in reorg_vals:
    numxs = row.count("X")

    if numxs == 1:
        if row[0] == "X":
            row[0] = int(row[1]) - (int(row[2]) - int(row[1]))
        elif row[1] == "X":
            row[1] = (int(row[0]) + int(row[2])) / 2
        else:
            row[2] = int(row[1]) - int(row[0]) + int(row[1])

final_vals = [[reorg_vals[0][0], reorg_vals[1][0], reorg_vals[2][0]],
              [reorg_vals[0][1], reorg_vals[1][1], reorg_vals[2][1]],
              [reorg_vals[0][2], reorg_vals[1][2], reorg_vals[2][2]]]

for row in final_vals:
    print(int(row[0]), int(row[1]), int(row[2]))
