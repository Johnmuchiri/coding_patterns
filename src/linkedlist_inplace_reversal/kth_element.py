import unittest
"""
Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the kkth to last node in the list.

For example:

  class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
kth_to_last_node(2, a)

"""

def kth_to_last_node(k, head):
    # Return the kth to last node in the linked list

    current = head
    pos = k
    n = 0

    while current:
        current = current.next
        n += 1

    if k > n:
        return None

    kth_position = (n - k)
    current_1 = head
    while kth_position > 0:
        current_1 = current_1.next
        kth_position -= 1
    return current_1









