'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteHead(head):
    #code here
    # Check if the linked list is empty
    if not head:
        return None
    
    # If there's only one node in the circular linked list
    if head.next == head:
        del head
        return None
    
    # Find the node before the head
    prev = head
    while prev.next != head:
        prev = prev.next
    
    # Update the next pointer of the previous node to skip the head node
    prev.next = head.next
    
    # Update head to the next node and delete the original head
    new_head = head.next
    head.next = None
    del head
    
    return new_head