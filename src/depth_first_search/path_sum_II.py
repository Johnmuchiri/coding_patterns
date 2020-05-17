


"""

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        routes = []

        if root is None:
            return []

        def helper(root, target, prev_path):

            prev_path.append(root.val)
            if not root.right and not root.left and root.val == target:
                routes.append(prev_path)

            if root.right:
                helper(root.right, target - root.val, prev_path)

            if root.left:
                helper(root.left, target - root.val, prev_path)

        helper(root, sum, [])

        return routes





