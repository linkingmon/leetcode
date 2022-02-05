# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ori_head = head
        carry = 0
        while True:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            sum = l1_val + l2_val + carry
            head.val = sum % 10
            carry = sum // 10
            head.next = ListNode()
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            if(l1 is None and l2 is None):
                if carry == 0:
                    head.next = None
                else:
                    head.next.val = carry
                break
            head = head.next
        return ori_head