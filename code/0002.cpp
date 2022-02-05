// Codes for 
//     2. Add Two Numbers
// Author : Yu-Cheng Lin 
//          2021. 12. 20 - version 1 
// Complexity : O(n)

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        short quo = 0, rem;
        bool start = true;
        ListNode *head, *cur, *test;
        while(1){
            short sum = (l1==nullptr ? 0 : l1->val) + (l2==nullptr ? 0 : l2->val) + quo;
            quo = sum / 10;
            rem = sum - quo * 10;
            bool last = (l1 == nullptr && l2 == nullptr);
            if(!start && !(last && rem==0)) 
                {cur->next = new ListNode(rem); cur->next->val = rem;}
            if(start) {cur = new ListNode(rem); head = cur; start = false;}
            else cur = cur->next;
            if(last) break;
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
        }
        return head;
    }
};