#include <iostream>
#include <vector>
using namespace std;




class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        
        for (auto& row : box){

            int dropPos = row.size() - 1;

            for (int currPos = dropPos; currPos >-1; currPos--){

                if (row[currPos] == '*'){
                     dropPos = currPos - 1;

                }
                else if (row[currPos] == '#'){
                    swap(row[dropPos], row[currPos]);
                    dropPos --;
                }
               
            }
        }

        int rows = box.size();
        int cols = box[0].size();

        vector<vector<char>> rotatedBox(cols, vector<char>(rows));

        for (int i = 0; i < rows ; i++){

        for (int j = 0; j < cols ; j++){
        
        rotatedBox[j][rows - 1 - i] = box[i][j];
        }
        }

        return rotatedBox;

        
    }
};