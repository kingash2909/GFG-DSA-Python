
from collections import Counter

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        if len(s) < len(p):
            return "-1"
        
        p_freq = Counter(p)
        window_freq = Counter()
        min_window_length = float('inf')
        min_window_start = 0
        matched_chars = 0
        
        left = 0
        right = 0
        
        while right < len(s):
            window_freq[s[right]] += 1
            
            if s[right] in p_freq and window_freq[s[right]] == p_freq[s[right]]:
                matched_chars += 1
            
            while matched_chars == len(p_freq) and left <= right:
                if right - left + 1 < min_window_length:
                    min_window_length = right - left + 1
                    min_window_start = left
                
                window_freq[s[left]] -= 1
                if s[left] in p_freq and window_freq[s[left]] < p_freq[s[left]]:
                    matched_chars -= 1
                
                left += 1
            
            right += 1
        
        if min_window_length == float('inf'):
            return "-1"
        
        return s[min_window_start:min_window_start + min_window_length]
