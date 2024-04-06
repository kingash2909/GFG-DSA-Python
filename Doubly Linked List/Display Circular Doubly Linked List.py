
def displayList(head):
    #code here
    if not head:
        return []

    # List to store the elements of the circular doubly linked list
    elements_forward = []
    elements_backward = []

    # Traverse the circular doubly linked list from head to tail
    current = head
    while True:
        elements_forward.append(current.data)
        current = current.next
        if current == head:  # Break if we reach the head again
            break

    # Traverse the circular doubly linked list from tail to head
    current = head.prev  # Start from the tail
    while current != head:  # Stop when we reach the head
        elements_backward.append(current.data)
        current = current.prev

    # Return the list representing the circular doubly linked list
    return elements_forward