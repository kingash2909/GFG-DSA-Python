
#Function to construct the BST from its given level order traversal.
def constructBst(arr,n):
    #Your code here
    
    if n == 0:
        return None
    root = Node(arr[0])
    for i in range(1, n):
        insert_node(root, arr[i])
    return root


def insert_node(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
    return root
    
    