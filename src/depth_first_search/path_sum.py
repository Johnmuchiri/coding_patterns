# Depth First Search
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \     \
7    2      1
return true, as there exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which sum is 22.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def path_sum(root: TreeNode, sum: int):
    if root is None:
        return False
    if root.val == sum and root.left is None and root.right is None:
        return True
    return path_sum(root.right, sum - root.val) or path_sum(root.left, sum - root.val)
