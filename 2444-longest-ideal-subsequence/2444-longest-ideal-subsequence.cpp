#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int longestIdealString(string s, int k) {

        
        

        vector<int> dp(26,0);


        for (char c : s){
            int idx = c - 'a';

            int max_prev = 0;

            for (int i = max(0,idx-k); i <= min(25, idx + k) ; i++){
                max_prev = max(max_prev, dp[i]);
            }

            dp[idx] = max(dp[idx], max_prev + 1);
        }
        return *max_element(dp.begin(), dp.end());
    }
};