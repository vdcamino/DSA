class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # - identify the nodes with 0 indegree (nodes that have no incoming edge/no prerequisites)
        # - traverse the graph starting from each one of these nodes
        # - if cycle detected, return false
        # - if len(visited) == numCourses: return True

        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        # build graph and indegree hashmap
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        # get nodes with no incoming edges
        nodes_with_no_incoming_edges = []
        for node in graph:
            if indegree[node] == 0:
                nodes_with_no_incoming_edges.append(node)

        # hashset to keep track of the nodes we have visited
        visited = set()

        # traverse the graph starting from the nodes with no incoming edges
        while len(nodes_with_no_incoming_edges) > 0:
            node = nodes_with_no_incoming_edges.pop()
            visited.add(node)
            for neighbour in graph[node]:
                # check for cycles
                if neighbour in visited:
                    return False
                # remove edge
                indegree[neighbour] -= 1
                # mark node as visited if it has no more prerequisites
                if indegree[neighbour] == 0:
                    nodes_with_no_incoming_edges.append(neighbour)

        return len(visited) == numCourses
