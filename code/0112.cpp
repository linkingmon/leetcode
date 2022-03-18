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
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root == nullptr) return false;
        bool res = false;
        check(root, 0, targetSum, res);
        return res;
    }
    void check(TreeNode* root, int sum, int& target, bool& res){
        if(root == nullptr) return;
        sum += root->val;
        if(root->left == nullptr && root->right == nullptr && sum == target) res = true;
        check(root->left, sum, target, res);
        check(root->right, sum, target, res);
    }
};