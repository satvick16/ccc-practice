import sys
from itertools import permutations, combinations

N, K = map(int, input().split())

nums = ""

for i in range(N):
    num = input()
    nums += num

of_concern = nums[:K]
perms = [''.join(i) for i in permutations(of_concern)]
perms.sort()

subs = []
x = [''.join(i) for i in combinations(nums, K)]
for p in x:
    subs.append(p)
subs = set(subs)

for perm in perms:
    if perm in subs:
        to_print = ""
        for char in perm:
            to_print += char + " "
        print(to_print[:-1])
        sys.exit()
