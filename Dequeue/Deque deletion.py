#User function Template for python3
from collections import deque

#Function to erase the element from specified position X in deque.
def eraseAt(deq,x):
    #code here
     if 0 <= x < len(deq):
        del deq[x]
#Function to erase the elements in range start (inclusive), end (exclusive).
def eraseInRange(deq,s,e):
    #code here
    if s == e:
        return
    deq.rotate(-s)  # Move the start index to the front
    for _ in range(e - s):
        deq.popleft()  # Remove elements in the specified range
    deq.rotate(s)  # Restore the original order

#Function to erase all the elements in the deque.   
def eraseAll(deq):
    #code here
    deq.clear()
