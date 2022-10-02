# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs.
# Other areas are safe to sail in. There are other explorers trying to find the treasure.
# So you must figure out a shortest route to the treasure island.

# Assume the map area is a two dimensional grid, represented by a matrix of characters.
# You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
# The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner.
# Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
# You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe.
# Output the minimum number of steps to get to the treasure.

# Example:

# Input:
# [['O', 'O', 'O', 'O'],
#  ['D', 'O', 'D', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['X', 'D', 'D', 'O']]

# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

# shortes path can be found using BFS
from collections import deque


def bfs(grid):
    q = deque()
    visited = set()
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q.append([0, (0, 0)])  # start at the origin
    path_list = [[(0, 0)]]  # list containing all the path we have passed
    path_index = int(
        0
    )  # index that will allow us to retrieve the shortest path from our path_list
    while q:
        current_path = path_list[path_index]
        aux = q.popleft()
        steps, y, x = aux[0], aux[1][0], aux[1][1]
        if grid[y][x] == "X":
            return steps, current_path
        visited.add((y, x))
        for dir in directions:
            dir_y, dir_x = y + dir[0], x + dir[1]
            if (
                dir_y in range(len(grid))
                and dir_x in range(len(grid[0]))
                and grid[dir_y][dir_x] != "D"
                and (dir_y, dir_x) not in visited
            ):
                new_path = current_path[:]  # create shallow copy of the current path
                new_path.append((dir_y, dir_x))
                path_list.append(new_path)
                q.append([steps + 1, (dir_y, dir_x)])

        # at the end of each node analysis, we continue to the next path in the list
        path_index += 1
    return -1


if __name__ == "__main__":
    # input matrix
    map = [
        ["O", "O", "O", "O"],
        ["D", "O", "D", "O"],
        ["O", "O", "O", "O"],
        ["X", "D", "D", "O"],
    ]
    nb_min_steps_from_treasure, path = bfs(map)
    print(nb_min_steps_from_treasure)
    print("minimum path is:", path)
