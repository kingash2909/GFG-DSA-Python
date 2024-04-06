
class Solution:
    ##Complete this function
    #Function to check if array is sorted and rotated.
    def checkRotatedAndSorted(self,arr,n):
        #code here
        # Initializing two variables x,y as zero.
        x = 0
        y = 0
     
        # Traversing array 0 to last element.
        # n-1 is taken as we used i+1.
        for i in range(n-1):
            if (arr[i] < arr[i + 1]):
                x += 1
            else:
                y += 1
     
        # If till now both x,y are greater than 1 means
        # array is not sorted. If both any of x,y is zero
        # means array is not rotated.
        if (y == 1):
            # Checking for last element with first.
            if (arr[n - 1] < arr[0]):
                x += 1
            else:
                y += 1
     
            # Checking for final result.
            if (y == 1):
                return True
     
        # If still not true then definitely false.
        return False