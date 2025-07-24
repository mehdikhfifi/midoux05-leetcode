class Solution {
public:
    int numDecodings(string s) {

        int n = s.size();

        vector<long> dp(n+1,0);

        dp[0] = 1;
        dp[1] = s[0] == '0' ? 0 : 1;

        for (int i = 1; i < n; i++){
            
            char character = s[i];
            char prev = s[i-1];
            int combination = (prev - '0' ) * 10 + (character - '0' );
            if (character == '0'){
                if (combination >= 10 && combination <= 26){
                    dp[i+1] = dp[i+1-2];
                }
                else{
                    dp[i+1] = 0;
                }
            }
            else{
                bool test = combination >= 10 and combination <= 26;
                cout << combination << '\n';
                if (combination >= 10 and combination <= 26){
                    dp[i+1] = dp[i+1-2] + dp[i+1-1];
                } 
                else{
                    dp[i+1] = dp[i+1-1];
            }

            for (auto x: dp) cout << x << ' ' ;
            cout << '\n';
            

            }
        }

        return dp[dp.size()-1];


        
        
    }
};

