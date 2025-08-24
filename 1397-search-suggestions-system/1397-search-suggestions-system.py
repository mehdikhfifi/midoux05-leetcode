

from typing import List


class Trie:
    def __init__(self,):
        self.top3 = []
        self.children = {}

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()
        
        # build our trie
        root = Trie()
        
        # insert each word into the trie
        
        def insert(word):
            temproot = root
            for char in word:
                if char not in temproot.children:
                    temproot.children[char] = Trie()
                temproot = temproot.children[char]
                if len(temproot.top3) <3:
                    temproot.top3.append(word)
        
        for product in products:
            insert(product)
        
        # return the result
        res: List[List[float]] = []
        broken = False
        node = root
        for char in searchWord:
            
            if char in node.children and not broken:
                node = node.children[char]
                res.append(node.top3)
            
            else:
                broken = True
                res.append([])
        return res