import sys

N, C, V = map(int, sys.stdin.readline().split())

word = input()

vowels = ['a', 'e', 'i', 'o', 'u']

vow = 0
con = 0

for c in range(len(word)):
    if word[c] == 'y':
        vow += 1
        con += 1
    else:    
        if word[c] in vowels:
            vow += 1
            con = 0
        else:
            con += 1
            vow = 0

    if vow > V or con > C:
        print("NO")
        sys.exit()

print("YES")
