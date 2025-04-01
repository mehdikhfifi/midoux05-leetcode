#include <iostream>




using namespace std;






class Solution {
    public: 

    int divide(int x , int y){



        if (x == INT_MIN && y == -1){
            return INT_MAX;
        }
        
        if (y == 0){
            std:throw overflow_error("Cannot divide by zero");
        }




        long long dividend = abs( (long long )x);
        long long divisor = abs( (long long ) y);


        int sign = (x > 0) ^ (y > 0) ? -1 : 1;

        long long quotient = 0;


        while (dividend >= divisor){


            long long multiple =1;
            long long temp = divisor;

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
