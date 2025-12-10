import math
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        

        if complexity.count(complexity[0]) > 1 or complexity[0] > min(complexity):
            return 0
        else:
            n = len(complexity)
            return math.factorial(n-1) % (10**9 + 7)