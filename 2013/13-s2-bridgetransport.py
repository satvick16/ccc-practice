import sys

W = int(input())
N = int(input())

weights = [0, 0, 0]

for i in range(N):
    weight = int(input())
    weights.append(weight)

counter = 0

for i in range(len(weights) - 3):
    sublist = weights[i:i+4]

    print(sum(sublist))
    print(counter)

    if sum(sublist) > W:
        if counter == 0:
            print(0)
            sys.exit()
        print(counter + 3)
        sys.exit()

    counter += 1

print(N)
