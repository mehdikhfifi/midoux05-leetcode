#include <iostream>
#include <string>
#include <vector>


using namespace std;


class Solution {
public:
    int divide(int x, int y) {
        
        if (x == INT_MIN && y == -1){
            return INT_MAX;
        }
        if (y == 0){
            throw runtime_error("cannot divide by zero");
        }

        int sign =  (x > 0) ^ (y > 0)  ? -1 : 1;

        long long dividend = abs((long long) x);
        long long divisor = abs((long long) y);

        long long quotient = 0;


        while (dividend >= divisor){

            long long temp = divisor;
            long long multiple = 1;

            while (dividend >= (temp << 1)){

                multiple <<=1;
                temp <<=1;
            }

            dividend -= temp;
            quotient += multiple;

        }

        return quotient * sign;
    }
};