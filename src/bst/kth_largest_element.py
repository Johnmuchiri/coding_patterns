##inorder traversal will have the items orderd in asc order
##reverse inroder traversal prints items in des order

import unittest

"""

Write a function to find the 2nd largest element in a binary search tree. ↴

Here's a sample binary tree node class:

  class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        
        """


def find_second_largest(root_node):
    # Find the second largest item in the binary search tree

    nodes = []

    def in_order_traversal_rec(root_node, nodes):
        if root_node is None:
            return
        in_order_traversal_rec(root_node.right, nodes)
        nodes.append(root_node.value)
        in_order_traversal_rec(root_node.left, nodes)

    in_order_traversal_rec(root_node, nodes)

    print(nodes)

    return nodes[1]




