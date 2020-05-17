
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        prev = None
        current = head
        while m > 1:
            prev = current
            current = current.next
            m -= 1
            n -= 1

        connection_node = prev
        tail_node = current

        while n:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            n -= 1
        if connection_node:
            connection_node.next = prev
        else:
            head = prev

        tail_node.next = current

        return head
