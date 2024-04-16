
class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n):
        # code here

        k={}
        for i in arr:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1
        m=max(k.values())
        ind=0
        ans=""
        for i in k.keys():
            if k[i]==m and arr.index(i)>=ind:
                ans=i
                ind=arr.index(i)
        return ans
        