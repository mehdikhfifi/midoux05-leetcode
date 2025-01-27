#include <iostream>


#include <map>
using namespace std;


class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {


        map<int, int> myhashmap;
        
        myhashmap[0] = -1;


        int total = 0;

        for (int i = 0 ; i < nums.size(); i++ ){

            total += nums[i];
            int remainder = total % k;

            if (myhashmap.count(remainder) ==  0){
                myhashmap[remainder] = i;
            }
            else if (i - myhashmap[remainder] > 1)
            {
                return true;
            }
            

        }
        return false;


    }
};
