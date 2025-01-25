#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int lenw1 = word1.length();
        int lenw2 = word2.length();

        // Create a DP matrix with dimensions (lenw1 + 1) x (lenw2 + 1)
        vector<vector<int>> matrix(lenw1 + 1, vector<int>(lenw2 + 1, 0));

        // Initialize the first row and column
        for (int i = 0; i <= lenw1; i++) {
            matrix[i][0] = i; // Deleting all characters in word1
        }
        for (int j = 0; j <= lenw2; j++) {
            matrix[0][j] = j; // Inserting all characters in word2
        }

        // Fill the DP matrix
        for (int i = 1; i <= lenw1; i++) {
            for (int j = 1; j <= lenw2; j++) {
                int cost = (word1[i - 1] == word2[j - 1]) ? 0 : 1;
                matrix[i][j] = min({
                    matrix[i][j - 1] + 1,    // Insertion
                    matrix[i - 1][j] + 1,    // Deletion
                    matrix[i - 1][j - 1] + cost // Replacement
                });
            }
        }

        // Return the result in the bottom-right corner
        return matrix[lenw1][lenw2];
    }
};
