# User function Template for python3

'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''

#Function to make binary tree from linked list.
def convert(head):
  
    # code here
    q = []

    #base case
    if head is None:
        root = None
        return

    #the first node is always the root node so we add it to the queue.
    root = Tree(head.data)
    q.append(root)

    head = head.next

    #using a loop until we reach end of the linked list.
    while (head):

        #storing the front node from queue and removing it from queue.
        parent = q.pop(0)

        #taking next two nodes from the linked list and adding them as 
        #children of the current parent node. Pushing them into the queue
        #so that they will be parents to the future nodes.
        leftChild = None
        rightChild = None

        leftChild = Tree(head.data)
        q.append(leftChild)
        head = head.next
        if (head):
            rightChild = Tree(head.data)
            q.append(rightChild)
            head = head.next

        #assigning left and right children of parent node.
        parent.left = leftChild
        parent.right = rightChild
    return root
