from collections import defaultdict
from math import comb
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        hashmap = defaultdict(list)
        for x,y in points:
            
            hashmap[y].append((x,y))
        array = [comb(len(x),2) % MOD for x in hashmap.values()]

        tmp = sum(array)
        reversed_prefix = []

        for x in array:
            tmp -= x
            reversed_prefix.append(tmp)
        res = 0
        for i in range(len(array)):
            res += reversed_prefix[i] * array[i] % MOD


        return res % MOD