T = int(input())

data = []

for i in range(T):
    N = int(input())
    row = []

    for i in range(N):
        x = int(input())
        row.append(x)

    data.append(row)

def check(row):
    _ = row.copy()
    _.sort()
    lake = [0]
    branch = []

    while True:
        if len(row) > 0:
            if row[-1] == lake[-1] + 1:
                x = row[-1]
                row.pop(-1)
                lake.append(x)
                continue

        if len(branch) > 0:
            if branch[-1] == lake[-1] + 1:
                x = branch[-1]
                branch.pop(-1)
                lake.append(x)
                continue
        
        if len(row) > 0:
            x = row[-1]
            row.pop(-1)
            branch.append(x)
            continue

        lake.pop(0)
        
        if _ == lake:
            return True
        else:
            return False

for row in data:
    if check(row):
        print("Y")
    else:
        print("N")
