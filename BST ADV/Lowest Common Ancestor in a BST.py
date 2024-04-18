#Function to find the lowest common ancestor in a BST. 
def LCA(root, n1, n2):
    #code here.
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left_lca = LCA(root.left, n1, n2)
    right_lca = LCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca