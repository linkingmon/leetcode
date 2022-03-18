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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = new ListNode(0, head);
        ListNode* second = head;
        head = first;
        for(int i = 0 ; i < n - 1 ; ++i) second = second->next;
        while(second->next != nullptr){
            first = first->next;
            second = second->next;
        }
        first->next = first->next->next;
        return head->next;
    }
};