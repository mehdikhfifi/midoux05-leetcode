class Solution:
    def isUgly(self, n: int) -> bool:
        


        if n <= 0:
            return False

        prime_factors = [2,3,5]

        for factor in prime_factors:
            while n % factor ==0:
                n //= factor
        return n == 1