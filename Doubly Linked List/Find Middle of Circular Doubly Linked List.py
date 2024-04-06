class Solution:
    def findMiddle(self, head):
        #code here
        if head is None:
            return None
        
        # Initialize slow and fast pointers
        slow_ptr = head
        fast_ptr = head
        
        # Move fast pointer two steps and slow pointer one step at a time
        while fast_ptr.next != head and fast_ptr.next.next != head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # If the number of nodes is odd, slow pointer will be at the middle node
        # If the number of nodes is even, slow pointer will be at the first middle node
        return slow_ptr.data
