#include <iostream>
#include <vector>
#include <cmath> // for abs() with floating-point numbers
#include <cstdlib> // for abs() with integers

#include <limits>

//your code here



class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        

        long total_sum = 0;

        int num_negative = 0;

        int minimum = std::numeric_limits<int>::max();



        for (auto row : matrix){

            for( auto value: row){

                total_sum += abs(value);

                minimum = min(abs(value), minimum);

                if (value < 0){
                    num_negative +=1;
                }

            }

        }


        if (num_negative % 2 != 0){
            total_sum -= 2 * minimum;
        }

        return total_sum;



    }
};