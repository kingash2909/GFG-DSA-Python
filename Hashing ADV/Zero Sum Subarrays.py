
class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        
        m = {}
        cur_sum = 0
        count = 0
        
        for num in arr:
            cur_sum += num
            if cur_sum == 0:
                count += 1
            if cur_sum in m:
                count += m[cur_sum]
            m[cur_sum] = m.get(cur_sum, 0) + 1
        
        return count
        
        #return: count of sub-arrays having their sum equal to 0