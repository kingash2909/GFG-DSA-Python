#User function Template for python3

from collections import deque
dq = deque()

#dq : deque in which element is to be pushed
#x : element to be pushed


#Function to push element x to the front of the deque.
def push_front_pf(dq,x):
    #code here
    dq.appendleft(x)
    # print(x)

#Function to push element x to the back of the deque.
def push_back_pb(dq,x):
    #code here
    dq.append(x)
    # print(x)
    
#Function to return element from front of the deque.
def front_dq(dq):
    #code here
    if dq:
        return dq[0]
    else:
        return -1
    
#Function to pop element from back of the deque.
def pop_back_ppb(dq):
    #code here
    if dq:
        dq.pop()
    # print(front_dq(dq))
