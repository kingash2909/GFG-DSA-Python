
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def getLength(head):
    #code here
    if not head:
        return 0
    
    # Initialize length to 1 to count the first node.
    length = 1
    current = head.next
    
    # Traverse the circular linked list until we reach the head node again.
    while current != head:
        length += 1
        current = current.next
    
    return length