# maximum sum in array path

N = int(input())

triangle = []

for i in range(1, N+1):
    triangle.append(list(map(int, input().split())))

highest_sum = [[0 for j in range(i)] for i in range(1, N+1)]

highest_sum[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            highest_sum[i][j] = triangle[i][j] + highest_sum[i-1][0]
        elif j == i:
            highest_sum[i][j] = triangle[i][j] + highest_sum[i-1][-1]
        else:
            highest_sum[i][j] = triangle[i][j] + max(highest_sum[i-1][j-1], highest_sum[i-1][j])

print(max(highest_sum[-1]))

# minimum number of "clubs" ot reach set distance

distance = int(input())
num_clubs = int(input())

clubs = []

for i in range(num_clubs):
    clubs.append(int(input()))

strokes = [99999 for i in range(distance+1)]

strokes[0] = 0

for i in range(len(strokes)):
    for j in clubs:
        strokes[i] = min(strokes[i], strokes[i-j]+1)

if strokes[-1] != 99999:
    print("Roberta wins in {} strokes.".format(strokes[-1]))
else:
    print("Roberta acknowledges defeat.")
