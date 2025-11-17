using namespace std;

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int apart = 0;
        bool first_one = false;
     for (int i = 0; i < nums.size(); i++){
        if (nums[i] == 0 && first_one){
            apart +=1;
        }
        else if (nums[i] == 1){

            if (!first_one){
                first_one = true;
                continue;
            }
            else if (apart < k){
                return false;
            }
            apart = 0;
        }
     }   
     return true;
    }
};