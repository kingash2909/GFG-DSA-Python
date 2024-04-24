

class Solution:
    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self,ch):
    
        return ord(ch)-ord('a')
    
    #Function to insert string into TRIE.  
    def insert(self,root, key):
    
        pCrawl = root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
    
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
    
        #marking last node as leaf.
        pCrawl.isEndOfWord = True
    
    #Function to use TRIE data structure and search the given string.
    def search(self,root, key):
    
        pCrawl = root
        length = len(key)
        for level in range(length-1):
            index =self. _charToIndex(key[level])
            if not pCrawl.children[index]:
                return level
            pCrawl = pCrawl.children[index]
    
        if(pCrawl.isEndOfWord==False):
            return length-1
        return -1
    
    def check(self,lst, n):
        mp = {}
        root = self.getNode()
        for i in range(n):
            
            #searching if the string is already present in the trie or not.
            k = self.search(root, lst[i])
            s = lst[i]
            
            #if the string is present already in the trie we increase the
            #counter to count the number of times it appears in the trie.
            if (k==-1):
                if s not in mp:
                    mp[s]=1
                else:
                    mp[s]+=1
                print(s, end=" ")
                if(mp[s]>1):
                    print(mp[s])
                else:
                    print()
            else:
                
                #printing index upto which string can be uniquely identified.
                for j in range(k+1):
                    print(s[j], end="")
                    
                #inserting the string.
                self.insert(root, s)
                if s not in mp:
                    mp[s]=1
                else:
                    mp[s]+=1
                if(mp[s]>1):
                    print(mp[s])
                else:
                    print()
    
                
                    