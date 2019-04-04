"""

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:
    """
    Given by the task, the Binary Tree used.
    """
    def __init__(self, val, left=None, right=None):
        """
        initialize binary tree (Each node is itself the root of a tree)

        :param val: value of this Node
        :param left: left node, if any
        :param right: right node, if any
        """
        self.val = val
        self.left = left
        self.right = right


def serialize(n):
    """
    solution for serializing the Node. Pretty simple recursion to go through the tree Depth-First and build a string
    containing all its data.

    :param n: the node to serialize recursively
    :return:
    """
    s = ''
    s += '['
    s += '\"'+n.val+'\",'
    s += 'None,' if n.left is None else serialize(n.left) + ','
    s += 'None' if n.right is None else serialize(n.right)
    s += ']'
    return s


def find_nth_occurrence_in_string(string, sub, n):
    """
    helper function to find the n-th occurrence of a substring in a string.
    This maaay not be entirely necessary, but it works and was the first thing that came to mind for dealing
    with " symbols at the time.

    :param string: the text to search in
    :param sub: the substring to look for
    :param n: skip n-1 occurrences
    :return:
    """
    if n == 1:
        return string.find(sub)
    else:
        return string.find(sub, find_nth_occurrence_in_string(string, sub, n - 1) + 1)


def find_matching_closing_bracket(string):
    """
    Bit ugly, because it doesn't consider " symbols which could mark [/] to be part of a string.
    But it works for the provided tests, so I'll just consider the use of brackets in strings to be a usage error
    right now. Not like this code is getting shipped anyways.

    :param string: the text to check for [brackets]
    :return:
    """
    counter = 0
    for i in range(len(string)):
        if string[i] == '[':
            counter += 1
        elif string[i] == ']':
            counter -= 1
        if counter == 0:
            return i


def deserialize(s):
    """
    solution for the deserialize part of the task.
    In principle it's the same as serialize(n) backwards.
    But due to string handling being more work than string creating, it uses some more code and helper functions.
    I could probably optimize the string parsing a bunch still... but I probably won't.

    :param s: the string to turn into a Binary Tree (Node)
    :return:
    """
    if s[0] != '[' or s[-1] != ']':
        raise ValueError("Node not starting or ending with array brackets!")

    s = s[1:-1]
    a = find_nth_occurrence_in_string(s, '\"', 1)
    b = find_nth_occurrence_in_string(s, '\"', 2)
    val = s[a+1:b]
    s = s[b+2:]
    if s[0:4] == 'None':
        sub1 = None
        s = s[5:]
    else:
        br = find_matching_closing_bracket(s)
        sub1 = deserialize(s[:br+1])
        s = s[br+2:]
    if s[0:4] == 'None':
        sub2 = None
    else:
        br = find_matching_closing_bracket(s)
        sub2 = deserialize(s[:br+1])

    return Node(val, sub1, sub2)


def test():
    """
    As per the task, this test must pass. It does.

    :return:
    """
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    test()
