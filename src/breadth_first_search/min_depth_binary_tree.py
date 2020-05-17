"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        minDepth = 0
        if not root:
            return 0
        queue = [(minDepth + 1, root)]

        while len(queue):
            minDepth, curr = queue.pop(0)
            children = [curr.left, curr.right]
            if not any(children):
                return minDepth
            for c in children:
                queue.append((minDepth + 1, c))


