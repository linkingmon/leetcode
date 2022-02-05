# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr_1 = head
        if ptr_1 is None:
            return ptr_1
        ptr_2 = head.next
        if ptr_2 is None:
            return ptr_1
        out_head = ptr_2
        while True:
            if ptr_1 is None or ptr_2 is None:
                break
            ptr_1_next = ptr_2.next
            ptr_2.next = ptr_1
            if ptr_1_next is None:
                ptr_1.next = None
                break
            ptr_2_next = ptr_1_next.next
            ptr_1.next = ptr_2_next if ptr_2_next is not None else ptr_1_next
            ptr_1 = ptr_1_next
            ptr_2 = ptr_2_next
        return out_head