
"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here

        prev = None
        current = head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev  # New head of the reversed list
