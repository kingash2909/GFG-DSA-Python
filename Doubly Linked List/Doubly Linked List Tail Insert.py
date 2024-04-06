
def insertInTail(head,data):
    #code here
    new_node = Node(data)
    
    # If the list is empty, make the new node the head and tail
    if head is None:
        head = new_node
        return head
    
    # Traverse the list to find the tail node
    current = head
    while current.next is not None:
        current = current.next
    
    # Insert the new node after the tail
    current.next = new_node
    new_node.prev = current
    
    return head