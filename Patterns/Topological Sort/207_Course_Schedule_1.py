class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # - identify the nodes with 0 indegree (nodes that have no incoming edge/no prerequisites)
        # - traverse the graph starting from each one of these nodes
        # - if cycle detected, return False
        # - if len(visited) == numCourses: return True, else False

        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        # build graph and indegree hashmap
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # get nodes with no incoming edges
        nodes_in_degree_zero = []
        for course in graph:
            if in_degree[course] == 0:
                nodes_in_degree_zero.append(course)

        # variable to keep track of the visited nodes; hashset is not necessary for this problem
        visited = 0

        # traverse the graph starting from the nodes with no incoming edges
        while nodes_in_degree_zero:
            cur_node = nodes_in_degree_zero.pop()
            visited += 1
            for neighbor in graph[cur_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    nodes_in_degree_zero.append(neighbor)

        return visited == numCourses
