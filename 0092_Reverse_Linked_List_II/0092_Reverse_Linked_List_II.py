from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Nothing needs to be changed
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        leftPrevNode = dummy
        leftNode = head

        curIndex = 1

        # Get Left Node
        while curIndex < left:
            leftPrevNode = leftNode
            leftNode = leftNode.next
            curIndex += 1
        
        # Reverse
        prevNode = None
        curNode = leftNode
        while curIndex <= right:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            curIndex += 1

        # leftPrevNode.next is the end of the reversed node
        leftPrevNode.next.next = curNode
        leftPrevNode.next = prevNode

        return dummy.next