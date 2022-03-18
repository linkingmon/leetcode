/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == nullptr) return false;
        ListNode *fast, *slow;
        fast = slow = head;
        while(true){
            if(fast->next == nullptr || fast->next->next == nullptr) return false;
            ListNode *fast_next = fast->next->next;
            ListNode *slow_next = slow->next;
            if(fast_next == slow_next) return true;
            fast = fast_next;
            slow = slow_next;
        }
    }
};