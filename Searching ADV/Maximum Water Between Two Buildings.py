class Solution:
    
    #Function to return the maximum water that can be stored.
    def maxWater(self, height, n): 
        #Your code here
        left, right = 0, n - 1
        max_left, max_right = height[left], height[right]
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                water = max(water, (right - left - 1) * height[left])
                left += 1
                max_left = max(max_left, height[left])
            else:
                water = max(water, (right - left - 1) * height[right])
                right -= 1
                max_right = max(max_right, height[right])
        
        return water