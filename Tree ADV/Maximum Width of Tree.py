#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to get the maximum width of a binary tree.
    def getMaxWidth(self,root):
       
        #code here
        if not root:
            return 0

        max_width = 0
        q = deque()
        q.append(root)

        while q:
            level_size = len(q)

            # Update max_width if current level has more nodes
            max_width = max(max_width, level_size)

            # Iterate through current level nodes
            for _ in range(level_size):
                node = q.popleft()

                # Add left and right child to the queue if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return max_width

