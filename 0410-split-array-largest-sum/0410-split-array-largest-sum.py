import itertools

class Solution:
    def splitArray(self, weights: List[int], days: int) -> int:
        

        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high ) // 2
            num_trips = 1
            temp = 0
            for x in weights:
                if temp + x <= mid: 
                    temp +=x
                else: 
                    num_trips += 1
                    temp = x
            if num_trips <= days:
                high = mid 
            else:
                low = mid +1
        
        return low 


            
            
            

        

        






