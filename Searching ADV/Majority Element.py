
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        count = 0
        candidate = None
        
        for num in A:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        
        count = 0
        for num in A:
            if num == candidate:
                count += 1
        
        if count > N // 2:
            return candidate
        else:
            return -1  # No majority element found