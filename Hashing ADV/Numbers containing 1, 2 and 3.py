

def isValid(num):
    while num!=0:
        rem=num%10
        if rem!=1 and rem!=2 and rem!=3:
            return False
        num//=10
    return True
    
    
    
#Function to find all the numbers with only 1,2 and 3 in their digits.
def findAll():
    #code here
    for i in range(1,1000001):
        if isValid(i)==True:
            mp[i]=1
