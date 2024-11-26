from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        if n == 0:
            return -1

        


        hashmap = [0] * (n)

        for x,y in edges:
            hashmap[y] +=1

        
        m = [x for x in range(n) if hashmap[x] == 0 ]

        if len(m) == 1 :
            return m[0]
        return -1
        
        