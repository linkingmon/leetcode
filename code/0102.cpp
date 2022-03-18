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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        vector<vector<TreeNode*>> node_list;
        if(root == nullptr) return ans;
        ans.push_back(vector<int>(1,root->val));
        node_list.push_back(vector<TreeNode*>(1,root));
        while(true){
            vector<int> sub_ans;
            vector<TreeNode*> sub_node_list;
            for(int i = 0 ; i < node_list[node_list.size()-1].size() ; ++i){
                TreeNode* cur_node = node_list[node_list.size()-1][i];
                if(cur_node->left != nullptr){
                    sub_node_list.push_back(cur_node->left);
                    sub_ans.push_back(cur_node->left->val);
                }
                if(cur_node->right != nullptr){
                    sub_node_list.push_back(cur_node->right);
                    sub_ans.push_back(cur_node->right->val);
                }
            }
            if(sub_ans.size() == 0) break;
            ans.push_back(sub_ans);
            node_list.push_back(sub_node_list);
        }
        return ans;
    }
};