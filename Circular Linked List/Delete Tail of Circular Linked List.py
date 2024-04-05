
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def deleteTail(head):
    #code here
    if head is None:  # If list is empty, return None
        return None

    # If list has only one node, delete it and return None
    if head.next == head:
        return None

    # Traverse to the second-to-last node
    prev = None
    current = head
    while current.next != head:
        prev = current
        current = current.next

    # Update the next pointer of second-to-last node to point to head
    prev.next = head

    # Delete the last node
    del current

    return head  # Head remains unchanged