from collections import deque

'''
Function Arguments :
		@param  : q ( given queue to be used), k(Integer )
		@return : list, just reverse the first k elements of queue and return new queue
'''

#Function to reverse first k elements of a queue.

from queue import Queue


class Solution:
    def modifyQueue(self, q, k):
        # code here
        
        q2 = deque()
        for i in range(k):
            q2.append(q.popleft())
        q.extendleft(q2)
        return q