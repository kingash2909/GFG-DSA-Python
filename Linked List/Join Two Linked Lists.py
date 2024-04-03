'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def joinTheLists(head1, head2):
    #code here
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    # Find the last node of the first linked list
    current = head1
    while current.next is not None:
        current = current.next
    
    # Set the next pointer of the last node of the first list to the head of the second list
    current.next = head2
    
    return head1