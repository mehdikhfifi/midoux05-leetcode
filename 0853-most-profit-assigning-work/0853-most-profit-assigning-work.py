class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        

        jobs = sorted(zip(difficulty, profit))


        max_profit_at_difficulty = []

        max_profit = 0

        for d , p in jobs:

            max_profit = max(max_profit, p)
            max_profit_at_difficulty.append((d, max_profit))

        # this gets you the maximum profit you can get with a difficulty

        print(max_profit_at_difficulty)
        worker.sort()

        total_profit = 0

        job_idx =0 


        for ability in worker:

            while job_idx < len(max_profit_at_difficulty) and max_profit_at_difficulty[job_idx][0] <= ability:
                job_idx +=1
            # you obviously get the job_idx of the difficulty level just slightly 
            # unattainable by the respective worker
            if job_idx > 0:
                total_profit += max_profit_at_difficulty[job_idx -1][1]
        
        return total_profit
