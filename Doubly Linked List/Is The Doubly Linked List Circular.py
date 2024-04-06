
class Solution: 
    def isCircular(self, head):
        #code here

        # If the list is empty, it is not circular
        if head is None:
            return 0
        
        # Start traversing the list from the head node
        current = head.next
        while current is not None and current != head:
            current = current.next
        
        # If the current node is None, it means we reached the end of the list
        # without encountering the head node again, so the list is not circular
        if current is None:
            return 0
        else:
            return 1