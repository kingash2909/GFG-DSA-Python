
#Function to find the number of distinct combinations to reach the given score.
def count(score):
    
    #return: number of ways/combinations to reach the given score.
    dp = [0] * (score + 1)

    # Base cases
    dp[0] = 1  # There is one way to reach score 0 (by not making any move)

    # Calculate dp values
    for i in range(3, score + 1):
        dp[i] += dp[i - 3]  # If we make a move of 3 points
    for i in range(5, score + 1):
        dp[i] += dp[i - 5]  # If we make a move of 5 points
    for i in range(10, score + 1):
        dp[i] += dp[i - 10]  # If we make a move of 10 points

    return dp[score]