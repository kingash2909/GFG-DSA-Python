'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    #code here
    current = head
    
    while current is not None and current.next is not None:
        # If current node and next node have the same value, remove the next node
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    
    return head