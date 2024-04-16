'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        temp_map = {None: None}
        temp_head = head
        while temp_head:
            new_node = Node(temp_head.data)
            temp_map[temp_head] = new_node
            temp_head = temp_head.next
        temp_head = head
        while temp_head:
            temp_copy = temp_map[temp_head]
            temp_copy.next = temp_map[temp_head.next]
            temp_copy.arb = temp_map[temp_head.arb]
            temp_head = temp_head.next
        return temp_map[head]


