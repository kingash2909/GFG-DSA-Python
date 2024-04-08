class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num):
        node = self.root
        xor_result = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            if opposite_bit in node.children:
                xor_result |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return xor_result

class Solution:
    
    #Function to return maximum XOR value.
    def maxSubarrayXOR(self, arr, n):
        trie = Trie()
        max_xor = 0
        prefix_xor = 0
        trie.insert(0)
        for num in arr:
            prefix_xor ^= num
            max_xor = max(max_xor, trie.find_max_xor(prefix_xor))
            trie.insert(prefix_xor)
        return max_xor
