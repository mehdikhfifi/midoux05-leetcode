
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // m is the rows
        // n is the columns

        // first populate the grid with 1s in the sides
        using vec2d = vector<vector<int>>;

        vec2d matrix(m, vector<int>(n,0));
        
        for (int i = 0; i < m ; i++){
            matrix[i][0]  = 1;
        }
        for (int j = 0; j < n ; j++){
            matrix[0][j] = 1;
        }
        for (int i = 1; i < m; i++){
            for (int j = 1; j < n ; j++){
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1];
            }
        }
        return matrix[m-1][n-1];
    }
};