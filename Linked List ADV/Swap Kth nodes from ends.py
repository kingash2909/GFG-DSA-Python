'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes
		
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
#Function to swap Kth node from beginning and end in a linked list.
def swapkthnode(head,num,k):
    # return head of new linked list
    #code here
    if k > num or head is None:
        return head
        
    # Finding K th node from beginning
    curr1 = head
    prev1 = None
    i = 1
    while i< k:
        prev1 = curr1
        curr1 = curr1.next
        i+=1
        
    # Finding K th node from end   
    curr2 = head
    prev2 = None
    i=1
    while i < num-k+1:
        prev2 = curr2
        curr2 = curr2.next
        i+=1
    # No need to swap if the nodes are same
    if curr1 == curr2:
        return head
        
    # Update the next pointers of the previous nodes
    if prev1:
        prev1.next = curr2
    else:
        head=curr2
    
    if prev2:
        prev2.next = curr1
    else:
        head=curr1
    
    #Swap the nodes
    temp = curr1.next
    curr1.next = curr2.next
    curr2.next = temp
    
    return head