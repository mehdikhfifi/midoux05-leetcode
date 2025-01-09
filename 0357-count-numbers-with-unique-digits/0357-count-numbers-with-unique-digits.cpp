using namespace std;
#include <vector>
#include <iostream>
#include <iterator>



class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {

        if (n == 0){
            return 1;
        }
        
        if (n == 1){
            return 10;
        }

        vector<int> dp(n+1,0);

        dp[0] = 1;
        dp[1] = 10;

        for (int i = 2; i < n+1; i ++){

            int tobeadded = 1;

            int k = i;
            while (k!= 1){
                tobeadded *= (10 - (k-1));
                k-=1;
            }
            dp[i] = dp[i-1] + 9 * tobeadded;

        }
        return dp.back();
        
    }
};


