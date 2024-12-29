import itertools

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        

        diff = [0] * (n+1)


        for first, last, seats in bookings:
            diff[first-1] += seats
            if last < n:
                diff[last] -= seats

        result = [0] * n

        current_sum = 0

        return list(itertools.accumulate(diff))[:-1]

        # for i in range(n):
        #     current_sum += diff[i]
        #     result[i] = current_sum
        
        # return result
