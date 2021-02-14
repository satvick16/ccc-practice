import sys

N, C, V = map(int, sys.stdin.readline().split())

word = sys.stdin.readline()

vowels = ['a', 'e', 'i', 'o', 'u']

# checking vowels
for i in range(N - V):
    sub = word[i:i+V+1]

    counter = 0
    
    for j in sub:
        if j in vowels or j == 'y':
            counter += 1

            if counter > V:
                print("NO")
                sys.exit()

# checking consonants
for i in range(N - C):
    sub = word[i:i+C+1]

    counter = 0
    
    for j in sub:
        if j not in vowels or j == 'y':
            counter += 1

            if counter > C:
                print("NO")
                sys.exit()

print("YES")
