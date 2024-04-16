

#Function to find out the number of ways we can place a black and a white
#Knight on this chessboard such that they cannot attack each other.
def numOfWays(M, N):
    # code here
    #specifying the directions to check in i.e 8 directions.
    x_off = [-2,-2,-1, 1, 2, 2, 1, -1]
    y_off = [-1, 1, 2, 2, 1,-1, -2, -2]
    MOD = 1000000007

    #variable to maintain number of positions which are not feasible.
    ret = 0

    #iterating for complete matrix.
    for i in range(M):
        for j in range(N):
            for k in range(8):
                
                x = i + x_off[k]
                y = j + y_off[k]
                
                #checking if the attack position is within bounds.
                if x>=0 and x<M and y>=0 and y<N :
                    #if in bounds then it is not feasible so we increment.
                    ret+=1 
    
    #total possible combinations of 2 knights.
    total = ((M*N)*(M*N-1))%MOD 
    #returning total feasible combinations.
    return (total +MOD - ret)%MOD 