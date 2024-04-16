
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):

        if len(str1) != len(str2):
            return False
        mapping = {}
        mapped_chars=set()
        
        for i in range(len(str1)):
            if str1[i] not in mapping:
                if str2[i] in mapped_chars:
                    return False
                mapping[str1[i]]=str2[i]
                mapped_chars.add(str2[i])
            else:
                if mapping[str1[i]] != str2[i]:
                    return False
        return True