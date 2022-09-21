from collections import defaultdict
from collections import deque
from xmlrpc.client import boolean


def findBuildOrder(projects, dependencies):
    # build graph from dependencies list
    # some "unrelated projects" might be forgotten,
    # we will add them at the end,
    # their order doesn't make a diff...
    myGraph = defaultdict(list)
    # init state for each node
    for proj in projects:
        myGraph[proj].append("BLANK")
    for dep in dependencies:
        myGraph[dep[0]].append(dependencies[1])
    print(myGraph)
    # double ended queue that will contain the feasible order
    order = deque()
    # dfs that also verifies if the given node is currently part of a dfs path (cycle)
    def doDFS(project, order_stack):
        if myGraph[project][0] == "PARTIAL":
            return False  # cycle detected
        if myGraph[project][0] == "BLANK":
            myGraph[project][0] == "PARTIAL"
            for child in myGraph[project][
                1:
            ]:  # first element (0) is the state, so we start from index 1
                if not doDFS(child, order_stack):
                    return False
            myGraph[project][0] = "COMPLETE"
            order_stack.append(project)
        return True

    for project in projects:
        if myGraph[project][0] == "BLANK":
            if not doDFS(project, order):
                return None  # contain cycle
    return order


if __name__ == "__main__":
    projects = ("a", "b", "c", "d", "e", "f")
    dependencies = (("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c"))
    feasible_order = findBuildOrder(projects, dependencies).reverse()
    print(feasible_order)
