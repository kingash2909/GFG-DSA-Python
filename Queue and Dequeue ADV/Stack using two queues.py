#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue   
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    if queue_1.empty() and queue_2.empty():
        queue_1.put(x)
    else:
        if not queue_2.empty():
            queue_2.put(x)
        else:
            queue_1.put(x)

#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    if queue_1.empty() and queue_2.empty():
        return -1
    if not queue_1.empty():
        while queue_1.qsize() > 1:
            queue_2.put(queue_1.get())
        ans = queue_1.get()
        return ans
    else:
        while queue_2.qsize() > 1:
            queue_1.put(queue_2.get())
        ans = queue_2.get()
        return ans