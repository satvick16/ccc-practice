# Combinations formula
n = '''numberof objects'''
r = '''number of choosing objects'''

ncr = (fact(n)) / (fact(r) * fact(n - r))

# Permutations formula
n = '''numberof objects'''
r = '''number of choosing objects'''

npr = (fact(n)) / (fact(n - r))

# Filter values from list to avoid IndexError
data = list(filter(lambda a: '''condition which needs to be satisfied to be added to new list''', data))

# Get key from dict with max value
most_frequent = max(freqs, key=freqs.get)

# "Deep" copy of dict or list
import copy

old_dict = {1:"a", 2:"b"}
new_dict = copy.deepcopy(old_dict)

# Sum of list
x = sum(list_name)

# Delete item from dict
del dict_name[key]

# Remove duplicates from list
new_list = set(old_list)

# Sort 2D array by index
new_array = sorted(old_array, key=lambda old_array: old_array[index])

# Get list of permutations of a string
from itertools import permutations

list_name = [''.join(i) for i in permutations(string)]
