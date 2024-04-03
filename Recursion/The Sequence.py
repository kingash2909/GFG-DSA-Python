def theSequence(n):
    #code here
    if n == 0:
        return 1
    else:
        return n + n * theSequence(n-1)