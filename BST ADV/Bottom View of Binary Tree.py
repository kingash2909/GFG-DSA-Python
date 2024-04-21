
class Solution:
    def bottomView(self, root):
        # code here
        if root is None:
            return []
        
        # Initialize a dictionary to store the bottom view
        bottom_view = defaultdict(int)
        # Initialize a queue for level order traversal
        queue = deque()
        # Set the horizontal distance of root as 0
        root.hd = 0
        # Enqueue root
        queue.append(root)
        
        while queue:
            # Dequeue node from queue
            temp = queue.popleft()
            # Horizontal distance of the dequeued node
            hd = temp.hd
            
            # Update the bottom view
            bottom_view[hd] = temp.data
            
            # Enqueue left child with horizontal distance hd-1
            if temp.left:
                temp.left.hd = hd - 1
                queue.append(temp.left)
            # Enqueue right child with horizontal distance hd+1
            if temp.right:
                temp.right.hd = hd + 1
                queue.append(temp.right)
        
        # Sort the bottom view by horizontal distance and return the values
        return [bottom_view[key] for key in sorted(bottom_view)]
