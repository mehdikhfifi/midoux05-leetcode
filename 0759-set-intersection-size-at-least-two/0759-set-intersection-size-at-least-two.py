class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:


        intervals.sort(key =  lambda x : (x[1],-x[0]))
        print(intervals)

        a = -1
        b = -1
        ans = 0

        for interval in intervals:
            # print(f"interval[0] is {interval[0]} and interval[1] is {interval[1]}")
            if b < interval[0]:
                ans +=2
                a,b = interval[1]-1, interval[1]
            elif a < interval[0]:
                ans +=1
                a,b = b, interval[1]

        return ans
            

            


            
            
[1,3], [3,7], [8,9]

a = 2
b = 3