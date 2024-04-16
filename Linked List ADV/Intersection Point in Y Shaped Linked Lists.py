#User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #code here
    h1=head1
    h2=head2
    
    while h1!=h2:
        if h1==None:
            h1=head2
        if h2==None:
            h2=head1
        h1=h1.next
        h2=h2.next
    
    if h1==None:
        return -1
    return h1.data