#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here

    if not head:  # Empty linked list is considered circular
        return True

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True  # Cycle detected
        slow = slow.next
        fast = fast.next.next

    return False  # No cycle detected