N = input()
H = input()

freq = {}

for i in set(list(N)):
    freq[i] = list(N).count(i)

foo = set()
freq_new = {}

for i in set(list(H[:len(N)])):
    freq_new[i] = list(H[:len(N)]).count(i)

if freq_new == freq:
    foo.add(H[:len(N)])

for i in range(1, len(H) - len(N) + 1):
    freq_new[H[i-1]] -= 1

    if freq_new[H[i-1]] == 0:
        del freq_new[H[i-1]]

    if H[i:i+len(N)][-1] in freq_new:
        freq_new[H[i:i+len(N)][-1]] += 1
    else:
        freq_new[H[i:i+len(N)][-1]] = 1

    if freq_new == freq:
        foo.add(H[i:i+len(N)])

print(len(foo))
