class MyQueue:
    def __init__(self):
        self.stack1 = []  # For push operation
        self.stack2 = []  # For pop operation
        
    #Function to push an element x in a queue.
    def push(self, x):
         
         #add code here
            self.stack1.append(x)

    #Function to pop an element from queue and return that element.
    def pop(self): 
         
         # add code here
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            return -1
        
        # Pop the top element from stack2
        return self.stack2.pop()