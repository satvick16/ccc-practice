import sys

N, M = map(int, sys.stdin.readline().split())

room = []

for i in range(N):
    x = sys.stdin.readline()
    row = []

    for char in x:
        row.append(char)

    room.append(row)

for i in range(N):
    for j in range(M):
        if room[i][j] == "S":
            dots = []
            
            queue = []
            visited = []
            distance = []

            for m in range(N):
                row = []
                for n in range(M):
                    row.append(0)
                distance.append(row)

            start = [i, j]
            visited.append([i, j])
            distance[i][j] = 0
            queue.append([i, j])

            while len(queue) > 0:
                s = queue.pop(0)

                options = [[s[0]-1, s[1]], [s[0]+1, s[1]],
                           [s[0], s[1]-1], [s[0], s[1]+1]]

                for option in options:
                    if [option[0], option[1]] in visited or room[option[0]][option[1]] == "W":
                        continue

                    # check if camera is in line of sight

##                    surveilled = []
##
##                    for x in range(N):
##                        for y in range(M):
##                            if room[x][y] == "C":
##                                

                    if room[option[0]][option[1]] == ".":
                        d = abs(option[0] - s[0] + option[1] - s[1])

                        distance[option[0]][option[1]] = distance[s[0]][s[1]] + d

                        dots.append([distance[option[0]][option[1]], option[0], option[1]])
                        
                    visited.append([option[0], option[1]])
                    queue.append([option[0], option[1]])

            queue = []
            visited = []

            for m in range(N):
                for n in range(M):
                    if room[m][n] == ".":
                        dots_mod = []

                        for dot in dots:
                            dots_mod.append([dot[1], dot[2]])

                        if [m, n] in dots_mod:                            
                            for p in dots:
                                if [p[1], p[2]] == [m, n]:
                                    print(p[0])
                        else:
                            print(-1)
            
            sys.exit()
