#include <vector>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int longestIdealString(string s, int k) {
        


        vector<int> dp(26,0);


        for (char c: s){

            int index = c - 'a';

            int max_prev = 0;

            for (int i = max(0,index - k); i <= min(25,index + k); i++){
                
                max_prev = max(max_prev, dp[i]);
            }

            dp[index] = max(dp[index], max_prev +1) ;

        }
    return *max_element(dp.begin(), dp.end());
    }
};