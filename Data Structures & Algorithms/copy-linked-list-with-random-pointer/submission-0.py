"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first pass, create a deep copy and map the original -> copy
        originalToNew = {None: None}
        curr = head
        while curr:
            originalToNew[curr] = Node(curr.val)
            curr = curr.next

        # second pass, use the map to wire both the next and random pointers to the new nodes
        curr = head
        while curr:
            originalToNew[curr].next = originalToNew[curr.next]
            originalToNew[curr].random = originalToNew[curr.random]
            curr = curr.next
        return originalToNew[head]