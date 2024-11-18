#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> numbers(n,0);
        
        for (int i = 0; i < n; i ++){
            
            int value = 0;
            
            if (k > 0){
                for (int j = 1; j <= k ; j++){
                    value+= code[(i+j) % n];
                }
            }
            else if (k < 0){
                for (int j = 1; j <= -k ; j++){
                    value+= code[(i-j + n) % n];
                }
            }

            numbers[i] = value;

            
        };
        return numbers;
    }
};