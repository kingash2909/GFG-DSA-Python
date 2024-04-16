
#Function to find matching decimal representation of a string as on the keypad.
def printNumber(s,n):
   
    #CODE HERE
    keypad = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }
    
    # Initialize an empty string to store the decimal representation.
    decimal_representation = ""
    
    # Iterate through the characters in the string and map them to their decimal representations.
    for char in s:
        decimal_representation += keypad[char]
    
    # Return the final decimal representation as a string.
    return decimal_representation
