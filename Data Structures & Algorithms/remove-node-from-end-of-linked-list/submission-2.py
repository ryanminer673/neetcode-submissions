# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return head
            
        fast = head
        slow = head

        while fast and n > 1:
            fast = fast.next
            n-=1

        prev = None

        while fast.next: #TODO
            fast = fast.next
            prev = slow
            slow = slow.next

        if prev:
            prev.next = slow.next
        
        else:
            head = head.next

        return head


