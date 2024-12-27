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



class Solution {

private:

    vector<TreeNode*> generate(int start, int end){


        if (start > end){
            return {nullptr};
        }

        if (start == end){
            TreeNode* node = new TreeNode(start);
            return {node };
        }


        vector<TreeNode*> result;

        for (int val = start; val <= end; ++val) {

            vector<TreeNode*> leftTrees = generate(start, val -1);

            vector<TreeNode*> rightTrees = generate(val+1, end);


            for (auto leftSubtree : leftTrees){
                for (auto rightSubtree: rightTrees){
                    TreeNode* root = new TreeNode( val, leftSubtree, rightSubtree);
                    result.push_back( root);
                }
            }
        }
        return result;


    }


public:
    vector<TreeNode*> generateTrees(int n) {
        if (n==0){
            return{};
        }

        return generate(1,n);
        



    }
};