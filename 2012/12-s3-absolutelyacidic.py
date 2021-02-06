import sys

N = int(sys.stdin.readline())

data = []

for i in range(N):
    R = int(sys.stdin.readline())
    data.append(R)

freqs = {}

for i in set(data):
    freqs[i] = data.count(i)

if len(data) == len(set(data)):
    print(abs(max(data) - min(data)))
    sys.exit()

most_frequent = max(freqs, key=freqs.get)
data = list(filter(lambda a: a!= most_frequent, data))
del freqs[most_frequent]

second_most_frequent = max(freqs, key=freqs.get)
num_occ_sec_most_freq = data.count(second_most_frequent)
occs = [x for x, y in freqs.items() if data.count(x) == num_occ_sec_most_freq]

if len(occs) == 1:
    print(abs(most_frequent - second_most_frequent))
else:
    diffs = []
    
    for item in occs:
        diffs.append(abs(most_frequent - item))

    print(max(diffs))
