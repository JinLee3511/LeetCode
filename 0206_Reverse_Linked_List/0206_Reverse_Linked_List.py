from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Nothing, return the same list
        if not head:
            return head

        curNode = head
        prevNode = None
        nextNode = curNode.next

        # Reverse
        while curNode:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode

        return prevNode