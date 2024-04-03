
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def deleteHead(head):
    #code here
    if head is None:
        return None
    
    new_head = head.next
    head.next = None  # Set next pointer of the old head to None
    del head  # Delete the old head node
    
    return new_head