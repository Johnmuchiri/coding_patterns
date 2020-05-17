class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


##create a gap of k elements for one pointer and then move the two
# pointers one step each till the fast pointer hits the end

def kth_to_last_element(head, k):
    slow = head
    fast = head
    for i in range(k):
        fast = fast.next
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    return slow
