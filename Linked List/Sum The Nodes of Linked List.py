
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def sumOfElements(head):
    #code here
    total_sum = 0
    current = head
    while current is not None:
        total_sum += current.data
        current = current.next
    return total_sum