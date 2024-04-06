def insertInhead(head,data):
    #code here
    new_node = Node(data)
    
    # If the list is empty, make the new node the head
    if not head:
        head = new_node
        return head
    
    # Make the next of new node point to the current head
    new_node.next = head
    
    # Make the previous of current head point to the new node
    head.prev = new_node
    
    # Make the new node the new head
    head = new_node
    
    return head