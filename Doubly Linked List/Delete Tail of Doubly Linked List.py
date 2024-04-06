
def deleteTail(head):
    #code here
    # Case 1: If the list is empty
    if head is None:
        return None
    
    # Case 2: If the list has only one node
    if head.next is None:
        head = None
        return None
    
    # Traverse the list to find the second last node
    current = head
    while current.next.next is not None:
        current = current.next
    
    # Update the next pointer of the second last node to None
    current.next = None
    
    return head