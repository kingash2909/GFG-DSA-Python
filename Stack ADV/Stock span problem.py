
class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        stack = []
        res = []
        for i, p in enumerate(a):
            while stack and p >= stack[len(stack)-1][0]:
                stack.pop()
            if stack:
                res.append(i-stack[len(stack)-1][1])
            else:
                res.append(i+1)
            stack.append((p,i))
        return res