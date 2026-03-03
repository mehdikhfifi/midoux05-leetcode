class Solution {
public:
    int concatenatedBinary(int n) {
        

        long long bits = 0;
        long long res = 0;
        long long MOD = pow(10,9) + 7;

        for (int i = 1; i < n+1; i++){
            if ((i & i-1) == 0){
                bits++;
            }
            res = ((res << bits) | i) % MOD;
        }
        return res % MOD;
    }
};