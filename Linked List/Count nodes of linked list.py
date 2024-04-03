
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        #code here
        length = 0
        current = head_node
        while current is not None:
            length += 1
            current = current.next
        return length