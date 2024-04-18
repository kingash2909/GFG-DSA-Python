#Function to generate binary numbers from 1 to N using a queue.
from queue import Queue
def generate(N):
    # code here
    q = Queue()
    q.put('1')
    
    res = []
    for i in range(N):
        dequed_val = q.get()
        res.append(dequed_val)
        val1 = dequed_val + "0"
        val2 = dequed_val + "1"
        q.put(val1)
        q.put(val2)
    
    return res
    