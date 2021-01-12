import sys

def pretty_print(to_print):
    for i in to_print:
        print(i, end=" ")
    print()

N = int(input())

measurements = list(map(int, input().split()))

low = []
high = []

if N % 2 == 0:
    x = N // 2
else:
    x = N // 2 + 1

for i in range(x):
    low.append(min(measurements))
    measurements.remove(min(measurements))

low.reverse()
high = measurements
high.sort()

to_print = []

is_low = True

while True:
    if is_low:
        if len(low) == 0:
            pretty_print(to_print)
            sys.exit()
        to_print.append(low[0])
        low.pop(0)
        is_low = False
    else:
        if len(high) == 0:
            pretty_print(to_print)
            sys.exit()
        to_print.append(high[0])
        high.pop(0)
        is_low = True
