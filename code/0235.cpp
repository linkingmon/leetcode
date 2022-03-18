/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* ans;
    bool has_save = false;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        check(root, p, q);
        return ans;
    }
    bool check(TreeNode* root, TreeNode* p, TreeNode* q){
        if(root == nullptr) return false;
        bool find_l = check(root->left,p,q);
        bool find_r = check(root->right,p,q);
        bool root_is = false;
        if(root == p || root == q) {root_is = true;}
        if( (root_is && (find_l || find_r)) || (find_l && find_r) ) save(root);
        return find_l || find_r || root_is;
    }
    void save(TreeNode* root){
        if(!has_save) ans = root;
        has_save = true;
    }
};