"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []

        if not root:
            return []

        def get_paths(root, prev_nodes):

            prev_nodes += str(root.val)

            if not root.left and not root.right:
                paths.append(prev_nodes)

            prev_nodes += "->"
            if root.right:
                get_paths(root.right, prev_nodes)
            if root.left:
                get_paths(root.left, prev_nodes)

        get_paths(root, "")

        return paths
