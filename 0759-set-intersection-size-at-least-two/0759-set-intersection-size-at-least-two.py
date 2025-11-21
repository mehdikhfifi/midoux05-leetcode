class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:


        intervals.sort(key =  lambda x : (x[1], x[0]))
        print(intervals)

        a = -1
        b = -1
        ans = 0

        for interval in intervals:
            # print(f"interval[0] is {interval[0]} and interval[1] is {interval[1]}")
            print(interval)
            print(f"value of a is {a} and b is {b}")
            if not ( b >= interval[0] and b <= interval[1]):
                print("ans b is incrementing")
                ans += 1
                b = interval[1]
            if not (a >= interval[0] and a <= interval[1]):
                print("ans a is incrementing")
                ans += 1
                a = interval[1] if b != interval[1] else interval[1]-1
            a,b= min(a,b),max(a,b)
        return ans
            

            


            
            
[1,3], [3,7], [8,9]

a = 2
b = 3