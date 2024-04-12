import heapq

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        h = []
        row = len(arr)
        col = len(arr[0])
        
        for i in range(row):
            for j in range(col):
                heapq.heappush(h,arr[i][j])
                
        ansArr = []
        while h:
            ansArr.append(heapq.heappop(h))
            
        return ansArr