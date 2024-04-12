class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        totalCost = 0
        while len(arr) > 1:
            c1 = heapq.heappop(arr)
            c2 = heapq.heappop(arr)
            totalCost += c1 + c2
            heapq.heappush(arr, c1+c2)
        return totalCost
            