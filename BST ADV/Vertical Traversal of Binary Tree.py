from collections import defaultdict, deque


class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        if not root:
            return []
        
        # Dictionary to store nodes at each vertical level
        vertical_levels = defaultdict(list)
        
        # Queue for level order traversal
        queue = deque([(root, 0)])  # (node, vertical level)
        
        # Perform level order traversal
        while queue:
            node, level = queue.popleft()
            vertical_levels[level].append(node.data)
            
            if node.left:
                queue.append((node.left, level - 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Sort the levels and concatenate the nodes
        sorted_levels = sorted(vertical_levels.keys())
        result = []
        for level in sorted_levels:
            result.extend(vertical_levels[level])
        
        return result