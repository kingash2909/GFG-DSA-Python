#Function to return the lexicographically sorted power-set of the string.
def powerSet(s):
    #code here
    def backtrack(start, subset):
        result.append(''.join(subset))
        for i in range(start, len(s)):
            subset.append(s[i])
            backtrack(i + 1, subset)
            subset.pop()

    result = []
    backtrack(0, [])
    result.sort()  # Sort the result lexicographically
    return result
