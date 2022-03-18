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
    int maxDepth(TreeNode* root) {
        int max_val = 0;
        if(root == nullptr) return 0;
        traverse(root, 1, max_val);
        return max_val;
    }
    void traverse(TreeNode* mid, int level, int& max_val){
        if(mid->left != nullptr) traverse(mid->left,level+1,max_val);
        if(mid->right != nullptr) traverse(mid->right,level+1,max_val);
        max_val = max(level,max_val);
    }
};