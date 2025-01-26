


#include <iostream>
#include <unordered_map>

using namespace std;


class Solution{

    public:
    unordered_map<long , int> memo;
    
    int integerReplacement(int n){
         return integerReplacementHelper(static_cast<long >(n));
    }



    private:


    int integerReplacementHelper(long n ){

        if (n == 1) return 0;

        // if the number is already in memo then just go and find it there

        if (memo.find(n) != memo.end()) return memo[n];

        if ( n % 2 == 0){
            memo[n] = 1 +  integerReplacementHelper(n/2) ;
        }
        else{
            memo[n] = 1 + min(integerReplacementHelper(n+1), integerReplacementHelper(n-1));
        }


        return memo[n];

    }
};