# Q1. Given a list of item association relationships,
# write an algorithm that outputs the largest item association group.
# If two groups have the same number of items then select the group which
# contains the item that appears first in lexicographic order.

# Input :
# [[Item1, Item2], [Item3, Item4], [Item4, Item5]]

# Output :
# [Item3, Item4, Item5]

# approach
#   put the given list in the form of a graph (use adjacency list)
#   run a dfs and keep a curr_res_list for your dfs
#   also keep an overall res_list when performing dfs
#   if the length of your current dfs is greater than the res_list,
#       then your curr_res_list is the new res_list

from collections import defaultdict


def func(l):
    visited = []
    d = defaultdict(list)

    def dfs(item, output):
        if item not in visited:
            visited.append(item)
            output.append(item)
            for neighbor in d[item]:
                dfs(neighbor, output)

    if len(l) < 2:
        return l

    for item in l:
        if len(item) == 1:
            d[item[0]] = []
        else:
            d[item[0]].append(item[1])
            d[item[1]].append(item[0])

    res = []
    for item in d:
        if item not in visited:
            output = []
            dfs(item, output)
            output.sort()
            if len(res) == 0 or len(output) > len(res):
                res = output
            elif len(output) == len(res):
                res = min(res, output)

    return res


print(func([["A", "B"], ["D", "E"], ["C", "D"]]) == ["C", "D", "E"])
print(func([["A", "B"], ["C", "D"], ["F", "E"]]) == ["A", "B"])
print(func([["A", "B"], ["C", "D"], ["D", "E"], ["F", "E"]]) == ["C", "D", "E", "F"])
print(
    func([["A", "B"], ["C", "D"], ["D", "E"], ["F", "E"], ["A", "C"]])
    == ["A", "B", "C", "D", "E", "F"]
)
print(
    func(
        [
            ["A", "B"],
            ["F", "E"],
            ["G", "K"],
            ["C", "D"],
            ["D", "E"],
            ["X", "G"],
            ["X", "N"],
            ["K", "L"],
            ["L", "M"],
            ["F", "E"],
            ["A", "C"],
        ]
    )
    == ["A", "B", "C", "D", "E", "F"]
)
print(
    func([["item1", "item2"], ["item3", "item4"], ["item4", "item5"]])
    == ["item3", "item4", "item5"]
)
print(
    func([["item1", "item2"], ["item2", "item5"], ["item3"]])
    == ["item1", "item2", "item5"]
)
print(
    func(
        [["item1", "item2"], ["item2", "item3"], ["item4", "item5"], ["item5", "item6"]]
    )
    == ["item1", "item2", "item3"]
)
print(
    func(
        [
            ["item1", "item2"],
            ["item1", "item3"],
            ["item2", "item7"],
            ["item3", "item7"],
            ["item5", "item6"],
            ["item3", "item7"],
        ]
    )
    == ["item1", "item2", "item3", "item7"]
)

print(
    func(
        [["item1", "item2"], ["item1", "item4"], ["item3", "item4"], ["item4", "item5"]]
    )
)

print(
    func(
        [
            ["item3", "item4"],
            ["item1", "item2"],
            ["item5", "item6"],
            ["item4", "item5"],
            ["item2", "item7"],
            ["item7", "item8"],
        ]
    )
)

print(
    func(
        [["item1", "item2"], ["item3", "item4"], ["item5", "item6"], ["item4", "item5"]]
    )
)
