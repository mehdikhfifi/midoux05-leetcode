class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks) % 4 !=0:
            return False

        matchsticks.sort(reverse=True)


        sides = [0] * 4

        side_length =  sum(matchsticks) // 4

        def backtrack(index):
            nonlocal sides
            nonlocal side_length

            if index == len(matchsticks):
                return all(side == side_length for side in sides)

            for i in range(4):

                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index +1):
                        return True
                    
                    sides[i] -= matchsticks[index]
                
                if sides[i] ==0:
                    break
            return False
        

        return backtrack(0)
        


