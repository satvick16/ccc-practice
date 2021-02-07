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
