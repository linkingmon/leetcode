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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(root == nullptr)
            root = new TreeNode(val);
        else
            find(root, val);
        return root;
    }
    void find(TreeNode* root, int val){
        if(root->val > val){
            if(root->left == nullptr) root->left = new TreeNode(val);
            else find(root->left, val);
        }
        else{
            if(root->right == nullptr) root->right = new TreeNode(val);
            else find(root->right, val);
        }
    }
};