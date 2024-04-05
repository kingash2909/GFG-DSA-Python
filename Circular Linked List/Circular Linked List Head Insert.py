
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def insertInHead(head,x):
    #code here

    new_node = Node(x)

    if head is None:  # If list is empty, new node becomes the head itself
        new_node.next = new_node
        return new_node

    # Traverse to the last node of the list
    last = head
    while last.next != head:
        last = last.next

    # Insert new node before the head
    new_node.next = head
    last.next = new_node

    # Update head to new node
    return new_node