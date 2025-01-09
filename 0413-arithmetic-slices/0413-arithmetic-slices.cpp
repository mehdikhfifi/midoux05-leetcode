class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {

        int n = nums.size();

        if (n < 3){
            return 0;
        }

        int prev =0 ;
        
        int total_slices = 0;

        for (int i =2; i < n; i ++){

            if ((nums[i] - nums[i-1]) == (nums[i-1] - nums[i-2]) ){

                prev = prev + 1;
            } else{
                prev = 0;
            }

            total_slices += prev;

        }
        return total_slices;
        
    }
};