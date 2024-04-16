

class Solution:
    
    #Function to check if the given pattern exists in the given string or not.
    def search(self,p,s):
        #code here
        if s.find(p) != -1:
            return True
        else:
            return False