
class Solution:
    
    #Function to check if the given pattern exists in the given string or not.
    def search(self,p,s):
        #code here

        for i in range(len(s)-len(p)+1):
            if s[i:i+len(p)] == p:
                return 1
        return 0