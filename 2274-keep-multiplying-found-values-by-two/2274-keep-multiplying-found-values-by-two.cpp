class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        for (int x  : nums){
            if (x == original){
                return findFinalValue(nums, original *2);
            }
        }
        return original;
    }
};