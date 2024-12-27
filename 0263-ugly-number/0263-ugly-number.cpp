class Solution {
public:
    bool isUgly(int n) {

        if (n <= 0){
            return false;
        }


        int primes[3] = {2,3,5};

        for (int element: primes){

            while (n % element == 0){
                n = n / element;
            }
        }
        return n == 1;
        


    }
};