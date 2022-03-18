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
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root == nullptr) return nullptr;
        return find(root, val);
    }
    TreeNode* find(TreeNode* root, int val){
        TreeNode* ans1 = nullptr;
        TreeNode* ans2 = nullptr;
        if(root->val == val) return root;
        if(root->left != nullptr) 
            ans1 = find(root->left, val);
        if(root->right != nullptr) 
            ans2 = find(root->right, val);
        if(ans1 != nullptr) return ans1;
        else return ans2;
    }
};