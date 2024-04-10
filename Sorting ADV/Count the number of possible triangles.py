class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here

        count = 0
        arr.sort()
        for i in range(n-2):
            k = i+2
            for j in range(i+1,n-1):
                while k < n and arr[i]+arr[j] > arr[k]:
                        k += 1
                count += k - j - 1
        return count
        