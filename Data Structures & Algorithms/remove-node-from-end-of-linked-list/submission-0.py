# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # put fast n nodes ahead of slow
        for _ in range(n):
            fast = fast.next
        
        # move both until fast is on the last node
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # slow is just before the node to remove
        slow.next = slow.next.next
        return dummy.next