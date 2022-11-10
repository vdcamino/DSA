class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # - identify the nodes with 0 indegree (nodes that have no incoming edge/no prerequisites)
        # - traverse the graph starting from each one of these nodes
        # - if cycle detected, return False
        # - if len(visited) == numCourses: return True, else False

        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        # build graph and indegree hashmap
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # get nodes with no incoming edges
        nodes_in_degree_zero = []
        for course in graph:
            if indegree[course] == 0:
                nodes_in_degree_zero.append(course)

        # hashset to keep track of the nodes we have visited
        visited = set()

        # traverse the graph starting from the nodes with no incoming edges
        while nodes_in_degree_zero:
            cur_node = nodes_in_degree_zero.pop()
            visited.add(cur_node)
            for neighbor in graph[cur_node]:
                # check for cycles
                if neighbor in visited:
                    return False
                # remove edge
                indegree[neighbor] -= 1
                # mark node as visited if it has no more prerequisites
                if indegree[neighbor] == 0:
                    nodes_in_degree_zero.append(neighbor)

        return len(visited) == numCourses
