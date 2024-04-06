
def deleteHead(head):
    #code here

        # If the list is empty, return None
        if head is None:
            return None
        
        # If there's only one node in the list, delete it and return None
        if head.next is None:
            del head
            return None
        
        # Move the head pointer to the next node
        new_head = head.next
        
        # Set the previous of the new head to None
        new_head.prev = None
        
        # Set the next of the old head to None
        head.next = None
        
        # Delete the old head node
        del head
        
        return new_head