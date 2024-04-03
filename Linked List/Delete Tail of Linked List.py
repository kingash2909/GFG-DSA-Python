def deleteTail(head):
    #code here

    if head is None:
        return None
    
    # If the list has only one node, delete it and return None
    if head.next is None:
        del head
        return None
    
    # Traverse the list until the second-to-last node
    current = head
    while current.next.next is not None:
        current = current.next
    
    # Delete the last node and set the next pointer of the penultimate node to None
    del current.next
    current.next = None
    
    return head