
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def searchLinkedList(head,x):
    #code here
    current = head
    while current is not None:
        if current.data == x:
            return 1
        current = current.next
    return 0