/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        vector<ListNode*> vec;
        while(head != nullptr){
            if(head->val != val)
                vec.push_back(head);
            head = head->next;
        }
        if(vec.size() == 0) return nullptr;
        for(int i = 0 ; i < vec.size()-1 ; ++i)
            vec[i]->next = vec[i+1];
        vec[vec.size()-1]->next = nullptr;
        return vec[0];
    }
};