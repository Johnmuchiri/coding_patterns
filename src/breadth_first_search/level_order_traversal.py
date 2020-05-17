"""
LeetCode 102 - Binary Tree Level Order Traversal [medium]

Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

For example:

Given binary tree: [3, 9, 20, null, null, 15, 7]

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def level_order_traversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return []
        queue = [root]
        while len(queue) > 0:
            cur_level = []
            cur_level_size = len(queue)
            for i in range(cur_level_size):
                cur_node = queue.pop(0)
                cur_level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(cur_level)
        return res
