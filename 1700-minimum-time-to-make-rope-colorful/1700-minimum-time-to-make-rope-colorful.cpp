#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {

        int n = neededTime.size();

        vector<int> dp(n,0);

        for (int i = 1; i < n; i ++){

            if (colors[i-1] != colors[i]){
                dp[i] = dp[i-1];
            }
            else{
                dp[i] = dp[i-1] + min(neededTime[i], neededTime[i-1]);
                neededTime[i] = max(neededTime[i], neededTime[i-1]);
            }
        }
        return dp.back();

    }
};