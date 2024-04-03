
'''
class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
'''


#Function to return the decoded string.
def decodeHuffmanData(root, binaryString):
    #your code here
    result = ""
    current = root
    for bit in binaryString:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        
        if current.data != '$':
            result += current.data
            current = root

    return result