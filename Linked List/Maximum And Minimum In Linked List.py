
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def maximum(head):
    #code here
    if head is None:
        return None
    
    max_val = head.data
    current = head.next
    while current is not None:
        if current.data > max_val:
            max_val = current.data
        current = current.next
    return max_val
    
    
def minimum(head):
    #code here
    if head is None:
        return None
    
    min_val = head.data
    current = head.next
    while current is not None:
        if current.data < min_val:
            min_val = current.data
        current = current.next
    return min_val