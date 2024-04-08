

#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x // 2
        result = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1
        
        return result