class TopologicalSort:

    # Notes
    # 1. In-degree of a vertice in a graph = number of edges incident on this vertice (incoming edges)
    # 2. Graphs with cycles don't have a possible topological sort, because the cycle blocks the traversal
    # (the node that starts the cycle never reaches an in-degree value of zero)

    # Algorithm
    # - Identify nodes with no incoming edges
    # - Add these nodes to the ordering
    # - Decrement the in-degree of these nodes' neighbors
    # - Repeat

    # How to identify a cycle?
    # - Keep a set (or a simple variable) containing the nodes that are part of the current path
    # - If at the end of the traversal you didn't visit all the nodes, there is a cycle in the graph

    def topological_sort(digraph):
        # digraph (directed graph) represented as an adjacency list by a dictionary:
        #   key: a node
        # value: a set of adjacent neighboring nodes

        # build a dictionary mapping each node to its in-degree value
        in_degree = {node: 0 for node in digraph}
        for node in digraph:
            for neighbor in digraph[node]:
                in_degree[neighbor] += 1

        # track nodes with no incoming edges
        nodes_with_no_incoming_edges = []
        for node in digraph:
            if in_degree[node] == 0:
                nodes_with_no_incoming_edges.append(node)

        topological_sort = []

        # as long as there are nodes with no incoming edges
        # that can be added to the ordering
        while nodes_with_no_incoming_edges:

            # add one of those nodes to the ordering
            node = nodes_with_no_incoming_edges.pop()
            topological_sort.append(node)

            # decrement the indegree of this node's neighbors
            for neighbor in digraph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)

        # we've run out of nodes with no incoming edges
        # did we add all the nodes or find a cycle?
        if len(topological_sort) == len(digraph):
            return topological_sort  # got them all
        else:
            raise Exception("Graph has a cycle! No topological ordering exists.")
