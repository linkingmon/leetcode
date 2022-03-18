/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        vector<Node*> node_list;
        if(root != nullptr) node_list.push_back(root);
        while(node_list.size() != 0){
            for(int i = 0 ; i < node_list.size()-1 ; ++i)
                node_list[i]->next = node_list[i+1];
            vector<Node*> node_list_next;
            for(int i = 0 ; i < node_list.size() ; ++i){
                if(node_list[i]->left == nullptr) break;
                node_list_next.push_back(node_list[i]->left);
                node_list_next.push_back(node_list[i]->right);
            }
            node_list = node_list_next;
        }
        return root;
    }
};