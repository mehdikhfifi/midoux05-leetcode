
#include <iostream>

#include <vector>


using namespace std;

class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        // return length of longest wiggle subsequence 


        // how do you formulate dp problem

        // let dp[a][b] be the longest subsequence between indices a and b

        int n = nums.size();

        vector<int> up(n,1), down(n,1);

        if (n < 2) return n;
        // guaranteed to be wiggly


        for (int j = 1; j < n; ++j){
            for (int i = 0; i < j; ++i){
                if(nums[j]> nums[i]){
                    up[j] = max(up[j], down[i] +1);
                }
                else if (nums[j] < nums[i]){
                    down[j] = max(down[j], up[i] + 1);
                }
            }
        }

        return max(down[n-1], up[n-1]);


    }
};