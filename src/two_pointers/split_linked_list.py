class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def split(head):
    fast = head
    curr = head
    slow = curr

    while fast.next is not None:
        fast = fast.next.next
        curr = curr.next
        slow = curr
    slow.next = None
    half_one = head
    second_half = curr

    return [half_one, second_half]
