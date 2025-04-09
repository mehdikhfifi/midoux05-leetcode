#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int knightDialer(int n) {


        long long MODULO = 7 + 1e9 ;

        vector<vector<int>> moves = {
            {4, 6},    // 0
            {6, 8},    // 1
            {7, 9},    // 2
            {4, 8},    // 3
            {0, 3, 9}, // 4
            {},        // 5 (no valid knight moves to/from 5)
            {0, 1, 7}, // 6
            {2, 6},    // 7
            {1, 3},    // 8
            {2, 4}     // 9
        };

       
        vector<vector<int>> dp(n+1,vector<int>(10,0));

        cout << size(dp) << endl;

        for (int i = 0; i < 10 ; i++){
            dp[1][i] = 1;
        }

        // now we do the recursiveness

        for (int i = 2; i < n+1; i++){
            for (int digit = 0; digit < 10; digit++){
                for (int c: moves[digit]){

                    dp[i][digit] = (dp[i][digit] + dp[i-1][c] ) % MODULO;
                }

            }
        }
        int res = 0;
        for (int i = 0; i < 10; i ++){
            res = (res + dp[n][i]) % MODULO;
        }
        return res;
    }
};