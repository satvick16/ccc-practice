import sys

Y = int(input())

for year in range(Y + 1, 99999):
    year = list(str(year))
    year_copy = year.copy()
    
    year_copy.sort()

    duplicates = 0
    
    for i in range(len(year_copy) - 1):
        if year_copy[i] == year_copy[i + 1]:
            duplicates += 1

    if duplicates == 0:
        to_print = ""
        for num in year:
            to_print += num
        print(int(to_print))
        sys.exit()
