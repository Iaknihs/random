"""

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""


class Node:
    """
    To have something to work with I made myself a tree first!
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution_recursive(node):
    """
    Due to being recursive, this function assumes a tree that is not larger than the processors stack size.

    :param node: the root node to count from
    :return: number of unival subtrees
    """

    def count_unival_recursive(node):
        """
        I put this into a nested function, because for the final result we don't care if the root node is itself unival.
        Thus the outer function only returns the actual count, without the boolean.

        :param node: the node starting which to count unival subtrees
        :return: univality of this node, number of unival subtrees
        """
        if node.left is None:
            if node.right is None:
                return True, 1
            r_uni, count = count_unival_recursive(node.right)
            if r_uni and node.val == node.right.val:
                return True, count+1
            return False, count
        if node.right is None:
            l_uni, count = count_unival_recursive(node.left)
            if l_uni and node.val == node.left.val:
                return True, count+1
            return False, count
        r_uni, r_count = count_unival_recursive(node.right)
        l_uni, l_count = count_unival_recursive(node.left)
        if r_uni and l_uni and node.val == node.right.val == node.left.val:
            return True, r_count+l_count+1
        return False, r_count+l_count
    return count_unival_recursive(node)[1]


def solution_iterative(node):
    """
    Though I think the recusrive solution is more intuitive for trees, it doesn't always work.
    Thus: here's an iterative solution which should work regardless of tree size, assuming sufficient memory.

    :param node: the node starting which to count unival subtrees
    :return: number of unival subtrees
    """
    nodes = [node]
    unchecked = [node]
    # add all nodes of the tree to a list!
    while len(unchecked) > 0:
        n = unchecked[0]
        if n.left is not None:
            nodes.append(n.left)
            unchecked.append(n.left)
        if n.right is not None:
            nodes.append(n.right)
            unchecked.append(n.right)
        unchecked.pop(0)
    # Start at the leaves, count all unival nodes by marking the current node unival if its children are None or unival
    # and their values are the same as the current nodes.
    nodes = reversed(nodes)
    count = 0
    for n in nodes:
        if n.left is None or (n.left.unival and n.val == n.left.val):
            if n.right is None or (n.right.unival and n.val == n.right.val):
                n.unival = True
                count += 1
            else:
                n.unival = False
        else:
            n.unival = False
    return count


if __name__ == '__main__':
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(solution_recursive(tree))
    print(solution_iterative(tree))
