class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_palidrome(head):
    stack = []
    curr = head
    runner = head
    while runner is not None and runner.next is not None:
        stack.append(curr.val)
        curr = curr.next
        runner = runner.next.next
    if runner is not None:
        curr = curr.next
    while curr is not None:
        if stack.pop() != curr.val:
            return False
    return True



