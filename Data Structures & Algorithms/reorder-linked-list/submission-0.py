# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the middle node O(n) and break the linked list into 2 seperate ones
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow.next
        slow.next = None

        # reverse the second half of the list O(n)

        cur = middle
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        sec_half_rev_head = prev

        #build the new list alternating bewteen the first half and rev sec half
        first_half_head = head

        cur = head

        first_half_head = first_half_head.next

        while sec_half_rev_head:
            cur.next = sec_half_rev_head
            sec_half_rev_head = sec_half_rev_head.next
            cur = cur.next

            cur.next = first_half_head
            first_half_head = first_half_head.next
            cur= cur.next

            


    