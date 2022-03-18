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
    bool findTarget(TreeNode* root, int k) {
        vector<int> vec;
        check(root,vec);
        map<int,int> diff;
        for(int i = 0 ; i < vec.size() ; ++i){
            if(diff.find(vec[i]) != diff.end()) return true;
            else diff[k-vec[i]] = i;
        }
        return false;
    }
    void check(TreeNode* root, vector<int>& vec){
        if(root->left != nullptr) check(root->left,vec);
        vec.push_back(root->val);
        if(root->right != nullptr) check(root->right,vec);
    }
};