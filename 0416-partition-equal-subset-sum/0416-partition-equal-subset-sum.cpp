#include <numeric>


using namespace std;
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        

        int sum = accumulate(nums.begin(), nums.end(), 0);
        

        if (sum %2 != 0){
            return false;
        }
        int n = nums.size();
        int capacity = sum /2 ;

        vector< vector<bool>> dp( n+1 , vector<bool>(capacity+1, false) );
        

        for (int i = 0; i < n+1; i++){
            dp[i][0] = true;
        }
        for (int j = 1; j < capacity+1; j++){
            dp[0][j] = false;
        }

        for (int i = 1; i < n+1; i++){
            for (int j = 1; j < capacity+1; j++){
                dp[i][j] = dp[i-1][j];  // don't pick anything
                if (j >= nums[i-1]){
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]];
                }
            }
        }
        return dp[n][capacity];
    }
};