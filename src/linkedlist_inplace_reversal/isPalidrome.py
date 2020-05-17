
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        n = 0
        current = head
        while current is not None:
            current = current.next
            n += 1
        if n == 1:
            return True
        if n == 2 and head.val == head.next.val:
            return True
        else:
            return False

        ##reverse list

        prev = None
        nxt = None
        current = head

        while current.next is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        ##compare the tow linked lists
        rotated_head = prev
        unrotated_head = head
        while rotated_head.val != unrotated_head.val:
            return False

        return True


