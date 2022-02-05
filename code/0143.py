# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        slow_reverse_next = None
        odd_type = False
        if head.next is None:
            return
        while True:
            terminate = False
            slow_next = slow.next
            if fast.next is None :
                terminate = True
                odd_type = True
            elif fast.next.next is None:
                terminate = True
            else:
                fast = fast.next.next
            slow.next = slow_reverse_next
            slow_reverse_next = slow
            if terminate:
                break
            slow = slow_next
        if odd_type:
            head = slow
            slow = slow.next
            head.next = None
        else:
            head = None
        while True:
            slow_next__next = slow_next.next
            slow__next = slow.next
            slow_next.next = head
            slow.next = slow_next
            head = slow
            if slow_next__next is None:
                break
            slow_next = slow_next__next
            slow = slow__next