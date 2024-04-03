'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def displayList(head):
    #code here
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.next
    return result
    