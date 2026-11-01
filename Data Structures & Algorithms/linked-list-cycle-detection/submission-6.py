# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a fast slow pointer

        if not head or not head.next:
            return False
        
        fast = head.next
        slow = head

        while fast and fast.next:
            if fast.val == slow.val:
                return True

            fast = fast.next.next
            slow = slow.next

        return False