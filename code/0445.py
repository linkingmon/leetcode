# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_prev = None
        while True:
            l1_next = l1.next
            l1.next = l1_prev
            l1_prev = l1
            if l1_next is None: 
                break
            l1 = l1_next
        l2_prev = None
        while True:
            l2_next = l2.next
            l2.next = l2_prev
            l2_prev = l2
            if l2_next is None: 
                break
            l2 = l2_next
        tail = ListNode()
        carry = 0
        tail_prev = None
        while True:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            sum = l1_val + l2_val + carry
            tail = ListNode()
            tail.val = sum % 10
            tail.next = tail_prev
            tail_prev = tail
            carry = sum // 10
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            if(l1 is None and l2 is None):
                if carry != 0:
                    tail = ListNode()
                    tail.val = carry
                    tail.next = tail_prev
                break
        return tail