import sys
import math

# init the height and widht variables as well as the list containing each line of input (levels)
w, h = [int(i) for i in input().split()]
list_of_levels = list()

# iterate through the second -> last line input to add every line to our list of levels
for i in range(h):
    line = input()
    list_of_levels.append(line)

# retrieve starting points and add all of them to the list called list_of_starts
list_of_starts = list_of_levels[0].split("  ")

# retrieve end points and add them all to the list called list_of_ends
list_of_ends = list_of_levels[h-1].split("  ")

# create results list with list_of_starts (key) matching list_of_ends (value) for each index
results = list()

# traversing the levels list from each starting point
for current_start in list_of_starts:
    index_start = list_of_starts.index(current_start) * 3
    index_position = index_start
    k = index_start // 3
    # case where there is no change along the way
    results.append(list_of_starts[k] + list_of_ends[index_position // 3])
    # going down one level and verifying if change is needed
    for level in list_of_levels:
        # go to the left
        if index_position - 1 > 0 and level[index_position - 1] == "-":
            index_position -= 3
            results[k] = list_of_starts[k] + list_of_ends[index_position // 3]
        # go to the right
        elif index_position + 1 < w and level[index_position + 1] == "-":
            index_position += 3
            results[k] = list_of_starts[k] + list_of_ends[index_position // 3]

print(*results, sep="\n")
