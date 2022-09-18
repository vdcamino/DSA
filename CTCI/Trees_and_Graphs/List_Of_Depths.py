class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function that recursives with level + 1
def createLevelLinkedListRec_Aux(root, result_dict, level):
    # base case
    if root == None:
        return
    level_list = list()
    if len(result_dict) == level:  # level not contained in the list
        # levels are always traversed in order. So, if this is the first time we have visited level i,
        # we must have seen levels 0 through i - 1. We can therefore safely add the level at the end
        result_dict[level] = level_list
    else:
        level_list = result_dict.get(level)
    level_list.append(root)
    createLevelLinkedListRec_Aux(root.left, result_dict, level + 1)
    createLevelLinkedListRec_Aux(root.right, result_dict, level + 1)


# recursive implementation, a simple modification of inorder traversal -> we just pass the current level + 1 to the next recursive call
def createLevelLinkedListRec(root):
    result_dict = dict()
    createLevelLinkedListRec_Aux(root, result_dict, 0)
    return result_dict


# iterative implementation, using the list of parents for each level and addind their children to the next list
def createLevelLinkedList(root):
    result_list = list()
    current = list()
    # visit the root
    if root != None:
        current.append(root)
    while len(current) > 0:
        # add previous level to the result list
        result_list.append(current)
        parents = current  # keep track of the parents
        current = []  # clear the list because we are gonna traverse a new level
        for parent in parents:
            if parent.left != None:
                current.append(parent.left)
            if parent.right != None:
                current.append(parent.right)
    return result_list


if __name__ == "__main__":
    # init tree, node1 is the root
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(2)
    node4 = TreeNode(1)
    node5 = TreeNode(7)
    node1.left = node2
    node2.left = node3
    node1.right = node4
    node4.right = node5

    # print the result list
    # use lambda function to get the value of each node, than transform the map into a list so we can print it
    # for node in createLevelLinkedListRec(node1):
    #    result = list(map(lambda num: num.data, node))
    #    print(result)

    # get the result dictionary
    result_dict = createLevelLinkedListRec(node1)
    # apply map function to get the values of each node
    for i in result_dict:
        result = list(map(lambda x: x.data, result_dict.get(i)))
        # convert map to a list so we can print it
        print(result)
