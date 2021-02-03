import sys

n = int(sys.stdin.readline())

options = {}

for i in range(n):
    name, R, S, D = input().split()
    options[name] = 2 * int(R) + 3 * int(S) + int(D)

if len(options) == 1:
    print(list(options.keys())[0])
    sys.exit()

winners = {}

first = max(options, key=options.get)
winners[first] = options[first]
del options[first]
second = max(options, key=options.get)
winners[second] = options[second]

if winners[first] != winners[second]:
    print(first)
    print(second)
else:
    out = [first, second]
    out.sort()
    print(out[0])
    print(out[1])
