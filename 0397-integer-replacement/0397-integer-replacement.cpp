#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    unordered_map<long, int> memo; // Use long for memoization keys to handle overflow

    int integerReplacement(int n) {
        return integerReplacementHelper(static_cast<long>(n));
    }

private:
    int integerReplacementHelper(long n) {
        if (n == 1) return 0; // Base case: if n is 1, no operations are needed

        // If result is already computed, return it
        if (memo.find(n) != memo.end()) return memo[n];

        // If n is even, divide by 2
        if (n % 2 == 0) {
            memo[n] = 1 + integerReplacementHelper(n / 2);
        } else {
            // If n is odd, compute the minimum of n+1 or n-1 paths
            memo[n] = 1 + min(integerReplacementHelper(n + 1), integerReplacementHelper(n - 1));
        }

        return memo[n];
    }
};
