'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

#Function to return a tree created from postorder and inoreder traversals.
class Solution:
    def buildTree(self, In, post, n):
    # your code here
    
        def Btree(In,post,st,end,ind):
            if st>end:
                return None
            pos=map[post[ind]]
            root=Node(post[ind])
            root.right=Btree(In,post,pos+1,end,ind-1)
            root.left=Btree(In,post,st,pos-1,ind-(end-pos)-1)
            return root
        map={In[i]:i for i in range(n)}
        return Btree(In,post,0,n-1,n-1)