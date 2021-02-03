import random

num_vids = 10
nums = [x for x in range(1, num_vids+1)]

print(nums)

new_order = []

while len(nums) != 0:
    x = random.choice(nums)
    new_order.append(x)
    nums.remove(x)

print(new_order)
