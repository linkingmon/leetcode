# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        labeled = 1e5+1
        if head == None:
            return None
        while True:
            if (head.next == None or head.next.val == labeled):
                return head.next
            head.val = labeled
            head = head.next
        