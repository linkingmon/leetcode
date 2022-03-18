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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* ans = head;
        ListNode* rec = head;
        if(head == nullptr) return nullptr;
        while(true){
            ListNode* next = head->next;
            if(next == nullptr) {rec->next = nullptr; break;}
            if(next->val != rec->val) {rec->next = next; rec = next;}
            head = next;
        }
        return ans;
    }
};