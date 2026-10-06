# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        pre = None

        while(head.next != None):
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        
        head.next = pre

        return head

            