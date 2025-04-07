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

            // loop goes left to right and only extends subsequences using characters that have already been processed
            // what this looks like is that the dp[i] for characters that are ahead of c will be zero so it won't affect our max_prev

            for (int i = max(0,idx-k); i <= min(25, idx + k) ; i++){
                max_prev = max(max_prev, dp[i]);
            }
            // this for loop checks all the characters we can reasonably jump from in our sequence


            dp[idx] = max(dp[idx], max_prev + 1);
        }
        return *max_element(dp.begin(), dp.end());
    }
};