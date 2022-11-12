class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # create graph and in degree hashmap
        adj_list = {i: [] for i in range(1, n + 1)}
        in_degree = {i: 0 for i in range(1, n + 1)}

        # build graph and fill up in degree hashmap
        for prev_course, next_course in relations:
            adj_list[prev_course].append(next_course)
            in_degree[next_course] += 1

        # get nodes with in degree 0 (our starting points)
        nodes_in_degree_zero = collections.deque()
        for course in in_degree:
            if in_degree[course] == 0:
                nodes_in_degree_zero.append(course)

        # variable to keep track of the number of semesters
        res = 0

        # variable to check cycles
        visited = 0

        # traverse graph starting from nodes with in_degree = 0
        while nodes_in_degree_zero:
            nodes_in_this_level = len(nodes_in_degree_zero)
            visited += nodes_in_this_level
            while nodes_in_this_level:
                cur_node = nodes_in_degree_zero.popleft()
                for neighbor in adj_list[cur_node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        nodes_in_degree_zero.append(neighbor)
                nodes_in_this_level -= 1
            res += 1

        return res if visited == n else -1
