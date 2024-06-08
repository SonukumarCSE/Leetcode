class Node:
    def __init__(self):
        self.children = [None]*26
        self.eow = False
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True
    def search(self,key):
        curr = self.root
        for char in key:
            idx = ord(char) - ord('a')
            node = curr.children[idx]
            if node is None:
                return False
            curr = curr.children[idx]
        return curr.eow

class Solution:
    def __init__(self):
        self.trie = Trie()
        self.memo = {}
    def solve(self,key):
        if key in self.memo:
            return self.memo[key]
        if len(key) == 0:
            return True
        for i in range(1,len(key)+1):
            firstPart = key[0:i]
            secondPart = key[i:]
            if self.trie.search(firstPart) and self.solve(secondPart):
                self.memo[key] = True
                return True
        self.memo[key] = False
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            self.trie.insert(word)
        return self.solve(s)