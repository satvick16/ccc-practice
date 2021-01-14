K = int(input())

nums = []

for i in range(K):
    num = int(input())
    nums.append(num)

new_nums = []

for num in nums:
    if num != 0:
        new_nums.append(num)
    else:
        new_nums.pop()

sum_ = 0

for num in new_nums:
    sum_ += num

print(sum_)
