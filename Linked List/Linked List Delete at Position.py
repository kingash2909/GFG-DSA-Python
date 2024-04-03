
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteAtPosition(head, pos):
    #code here
    if head is None:
        return None
    
    # If the node to be deleted is the head node
    if pos == 1:
        new_head = head.next
        head.next = None  # Set next pointer of the old head to None
        del head  # Delete the old head node
        return new_head
    
    # Traverse the list to find the node just before the node to be deleted
    current = head
    for _ in range(pos - 2):
        if current is None or current.next is None:
            return head  # If position exceeds the length of the list, return the original head
        current = current.next
    
    # If the node to be deleted is not found, return the original head
    if current is None or current.next is None:
        return head
    
    # Update the next pointer of the node just before the node to be deleted
    next_node = current.next
    current.next = next_node.next
    
    # Delete the node to be deleted
    next_node.next = None
    del next_node
    
    return head