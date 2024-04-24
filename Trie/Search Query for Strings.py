
#Function to insert string into TRIE.    
def insert(root,key):
    temp = root
    for s in key:
        if temp.children[ord(s)-ord("a")]:
            temp = temp.children[ord(s)-ord("a")]
        else:
            new_node = TrieNode()
            temp.children[ord(s)-ord("a")] = new_node
            temp = new_node
    temp.isEndOfWord = True

#Function to use TRIE data structure and search the given string.
def search(root, key):
    temp = root
    
    for s in key:
        if not temp.children[ord(s)-ord('a')]:
            return False
        else:
            temp = temp.children[ord(s)-ord("a")]
    
    return temp.isEndOfWord