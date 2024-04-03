
class Solution:
    def printArrayRecursively(self,arr,n):
        #code here
        if n>0:
            self.printArrayRecursively(arr, n-1)
            print(arr[n-1], end=" ")