/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

 using namespace std;
 #include <iostream>
 #include <vector>
 #include <algorithm>
class Solution {
public:
    int longestZigZag(TreeNode* root) {
        
        return max(
            helper(root->right, false,0),
            helper(root->left, true,0)
        ) ;

        
    }

public:
    int helper(TreeNode* root, bool isLeft, int depth){

        if (root == nullptr){
            return depth;
        }

        if (isLeft){
            depth = max(
                helper(root->right, false, depth + 1),
                helper(root->left, true, 0)
                );
            
        }else{
            depth = max(
                helper(root->left, true, depth + 1),
                helper(root->right, false, 0)
                );

        }

        return depth;
    }
};