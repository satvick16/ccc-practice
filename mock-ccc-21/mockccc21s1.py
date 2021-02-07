letters = input()
string = input()

perms = []

#adding

for char in letters:
    for i in range(len(string)+1):
        x = string[:i] + char + string[i:]
        if x not in perms:
            perms.append(x)

#changing

for char in letters:
    for i in range(len(string)):
        if char != string[i]:
            x = string[:i] + char + string[i+1:]
            if x not in perms:
                perms.append(x)

#removing

for i in range(len(string)):
    x = string[:i] + string[i+1:]
    if x not in perms:
        perms.append(x)

#display

perms.sort()

for perm in perms:
    print(perm)
