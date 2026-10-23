# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        N = n + 1
        f = head

        while N > 0 and f:
            f = f.next
            N -= 1

        if N == 1:
            return head.next

        s = head

        while f:
            s = s.next
            f = f.next

        s.next = s.next.next

        return head
        


        