import sys
import copy

N = int(input())

nums = list(map(int, input().split()))

final = copy.deepcopy(nums)
final.sort()
final.reverse()

counter = 0

while True:
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            x = nums[i+1]
            nums[i+1] = nums[i]
            nums[i] = x
            counter += 1
    if nums == final:
        print(counter)
        sys.exit()
