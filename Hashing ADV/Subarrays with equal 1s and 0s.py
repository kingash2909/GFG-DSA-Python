
class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        m = {}
        cur_sum = 0
        count = 0
        
        for i in range(n):
            if arr[i] == 0:
                arr[i] = -1
                
        for i in range(n):
            cur_sum += arr[i]
            if cur_sum == 0:
                count += 1
            if cur_sum in m:
                count += m[cur_sum]
            m[cur_sum] = m.get(cur_sum, 0) + 1
        
        return count

