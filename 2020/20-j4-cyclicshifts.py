import sys

T = input()
S = input()

shifts = []

for i in range(len(S)):
    x = S[i:] + S[:i]
    shifts.append(x)

for i in range(len(T) - len(S) + 2):
    if T[i:i+len(S)] in shifts:
        print("yes")
        sys.exit()

print("no")
