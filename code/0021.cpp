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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        vector<ListNode*> node_vec;
        while(list1 != nullptr || list2 != nullptr){
            if(list1 != nullptr && (list2 == nullptr || list1->val < list2->val)) {
                node_vec.push_back(list1);
                list1 = list1->next;
            }
            else {
                node_vec.push_back(list2);
                list2 = list2->next;
            }
        }
        ListNode* head = nullptr;
        if(node_vec.size() > 0) head = node_vec[0];
        for(int i = 1 ; i < node_vec.size() ; ++i){
            node_vec[i-1]->next = node_vec[i];
        }
        return head;
    }
};