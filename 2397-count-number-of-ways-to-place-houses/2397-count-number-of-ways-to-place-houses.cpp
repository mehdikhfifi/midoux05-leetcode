#include <iostream>

#include <vector>

using namespace std;

class Solution {
public:
    int countHousePlacements(int n) {

        int MOD = pow(10,9) +7;

        vector<int> dp(n+1,0);

        dp[0] = 1;
        dp[1] = 2;
        for (int i = 2; i < n+1; i++){
            dp[i] = (dp[i-1] + dp[i-2] ) % MOD;
        }

        long long result = (1LL * dp[n] * dp[n]) % MOD;
        return static_cast<int>(result % MOD);
    }
};