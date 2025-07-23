#include <algorithm>

class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {


        int n = questions.size();
        vector<long long> dp(questions.size(), 0);

        

        dp[n-1] = questions[n-1][0];

        for (int i = n-2; i>= 0; i--){

            long long cur_q = questions[i][0];

            int next = questions[i][1] + i  + 1;


            if (next< questions.size()){
               cur_q += dp[next];
        }
        dp[i] = max(cur_q, dp[i+1]);
        }

        return *max_element(dp.begin(), dp.end());

    }
};