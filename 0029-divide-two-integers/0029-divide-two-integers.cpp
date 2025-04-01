#include <iostream>
#include <cmath>


using namespace std;


class Solution {
    public:
        int divide(int x, int y) {





            if (y == 0){
                throw std::overflow_error("division by zero");
            }

            if (x == INT_MIN && y == -1){
                return INT_MAX;
            }


            long long dividend = abs((long long )x);
            long long divisor = abs((long long ) y);

            int sign = (x > 0) ^ (y>0) ?  -1 : 1; // if they're the same sign will be 1 else -1




            long long quotient = 0;


            while (dividend >= divisor){


                long long  multiple = 1;
                long long temp = divisor;

                

                while (dividend >= (temp << 1)){

                    temp <<=1;
                    multiple <<=1;
                }

                quotient+= multiple;

                dividend -= temp;
            }
            
            return quotient * sign;
        }
    };