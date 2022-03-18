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
    bool isSymmetric(TreeNode* root) {
        vector<TreeNode*> node_list_left;
        vector<TreeNode*> node_list_right;
        if(root == nullptr || (root->left == nullptr && root->right == nullptr)) return true;
        bool res = true;
        check(root->left, root->right, res);
        return res;
    }
    void check(TreeNode* left, TreeNode* right, bool& res){
        if(left == nullptr && right != nullptr || left != nullptr && right == nullptr) 
            res = false;
        else if(left != nullptr && right != nullptr && right->val != left->val)
            res = false;
        else if(left != nullptr && right != nullptr){
            check(left->left,right->right,res);
            check(left->right,right->left,res);
        }
        
    }
};