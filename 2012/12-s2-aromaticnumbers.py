num = input()

ref = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

total = 0

flag = False

for i in range(len(num) - 1, 0, -2):
    val = ref[num[i]] * int(num[i-1])

    if flag:
        total -= val
    else:
        total += val

    if ref[num[i]] > ref[num[i-2]]:
        flag = True
    else:
        flag = False

print(total)
