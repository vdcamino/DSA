class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph (adj_list) + hashmap to keep track of the number of incoming edges for each node
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        # build edges + indegree
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # build a list containing only nodes with no incoming edges
        nodes_in_degree_zero = []
        for course in graph:
            if in_degree[course] == 0:
                nodes_in_degree_zero.append(course)

        # topological sort list keeping the visiting order
        top_sort = list()

        # traverse the graph starting from the nodes with no incoming edges
        while nodes_in_degree_zero:
            cur_node = nodes_in_degree_zero.pop()
            top_sort.append(cur_node)
            for neighbor in graph[cur_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    nodes_in_degree_zero.append(neighbor)

        return top_sort if len(top_sort) == numCourses else []
