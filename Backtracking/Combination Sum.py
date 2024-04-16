
class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
    
        # code here
        
        A = sorted(list(set(A)))
        result = []
        
        def backtrack(target_sum, start_index, current_combination):
            # once target sum has been reached, add combination to result
            if target_sum == 0:
                result.append(current_combination)
                return
            # otherwise, loop through A
            for i in range(start_index, len(A)):
                # ... and find a value that is less than the target
                if A[i] > target_sum:
                    break
                # update start_index to i to avoid reusing visited elements
                backtrack(target_sum - A[i], i, current_combination + [A[i]])
        
        backtrack(B, 0, [])
        return result