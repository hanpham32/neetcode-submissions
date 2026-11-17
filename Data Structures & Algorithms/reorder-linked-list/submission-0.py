# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        # count nodes
        N = 0
        temp = head
        while temp:
            temp = temp.next
            N += 1
        
        # find end of first half, then cut
        mid = head
        for _ in range((N-1)//2):
            mid = mid.next
        second = mid.next
        mid.next = None

        # reverse the second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # merge: one from each half, alternating 
        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2