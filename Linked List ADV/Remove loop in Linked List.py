'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes

        k={}
        h=head
        temp=None
        while h!=None:
            if h not in k:
                k[h]=1
            else:
                #if temp!=None:
                temp.next=None
                h=temp
            temp=h
            h=h.next
            
        return head