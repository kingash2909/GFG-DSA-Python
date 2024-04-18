#User function Template for python3

class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        #add code here
        st = []
        while(q.qsize()>0):
            st.append(q.get())
        while(len(st)>0):
            q.put(st.pop())
        return q
