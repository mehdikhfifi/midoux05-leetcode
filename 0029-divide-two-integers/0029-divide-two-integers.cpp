class Solution {
public:
    int divide(int x, int y) {


        // check for runtime errors

        if(y ==0){
            throw std::overflow_error("Division by zero");
        }

        if (x == INT_MIN && y == -1){
            return INT_MAX;
        }


        long long dividend = abs( (long long )x);
        long long divisor = abs( (long long ) y);
        long long quotient =0 ;

        long long sign = (x >0) ^ (y> 0) ? -1: 1;
        

        while (dividend >= divisor){
            

            long long temp = divisor;
            long long multiple = 1;

            while (dividend >= (temp << 1)){

                temp <<= 1;
                multiple <<=1;
            }
            dividend -= temp;
            quotient += multiple;
        }
        cout << quotient << endl;
        cout << sign << endl;

        return quotient * sign;



    }
};