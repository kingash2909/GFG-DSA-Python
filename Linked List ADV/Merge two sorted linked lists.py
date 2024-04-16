#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    head = Node(-1)
    dummy = head
    arr = []
    while head1 is not None:
        arr.append(head1.data)
        head1 = head1.next
    
    while head2 is not None:
        arr.append(head2.data)
        head2 = head2.next
        
    arr.sort()
    
    for i in range(len(arr)):
        head.next = Node(arr[i])
        head = head.next
    return dummy.next  
