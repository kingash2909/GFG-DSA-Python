'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        # If the list is empty or has only one node, no need to reverse
        if head is None or head.next is None:
            return head
        
        # Initialize pointers
        prev_node = None
        current_node = head
        
        # Traverse the list and reverse the pointers
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node
            current_node = next_node
        
        # Update the head pointer to point to the last node (which is now the first node after reversal)
        head = prev_node
        
        return head