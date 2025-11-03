class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:


        # i = 0
        # needed_time = 0
        # while i < len(colors):

        #     chosen_color = colors[i]
        #     chosen_time = neededTime[i]
        #     k = i +1
        #     res = [chosen_time]
        #     while k < len(colors) and colors[k] == chosen_color:
        #         res.append(neededTime[k])
        #         k+=1
        #     sum_res = sum(res)
        #     max_res = max(res)
        #     needed_time += sum(res) - max(res)
        #     i = k
        # return needed_time

        res = neededTime[0]
        max_i = neededTime[0]

        for i in range(1,len(colors)):
            if colors[i-1] != colors[i]:
                res -= max_i
                max_i = 0
            res += neededTime[i]
            max_i = max(max_i, neededTime[i])
        return res - max_i


        
