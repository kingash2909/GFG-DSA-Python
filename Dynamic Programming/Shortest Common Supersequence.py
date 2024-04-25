
class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        
         #code here
        #using dp[][] array to store length of shortest common supersequence.
        dp = [[0] * (n + 2) for i in
                        range(m + 2)] 
                        
        #dp[i][j] contains length of SCS of X[0..i-1] and Y[0..j-1].
          
        for i in range(m + 1): 
              
            for j in range(n + 1): 
                
                #if i is 0, dp[i][j] will be equal to size of second string.   
                if (i == 0):
                    dp[i][j] = j
                    
                #else if j is 0, dp[i][j] will be equal to size of first string. 
                elif (j == 0):
                    dp[i][j] = i
                    
                #if character of both strings are same then dp[i][j]
                #will be 1+ dp[i-1][j-1].
                elif (X[i - 1] == Y[j - 1]) : 
                    dp[i][j] = dp[i - 1][j - 1] + 1
                
                 #else dp[i][j] will be 1+ minimum answer without considering
                 #the current character of 2 strings.
                else :
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1]) 
        
        #returning the result.          
        return dp[m][n] 