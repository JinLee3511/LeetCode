from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        mergedList = ListNode()
        start = mergedList

        # Store Values that are smaller from each list
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                mergedList.next = list1
                list1 = list1.next
            else:
                mergedList.next = list2
                list2 = list2.next

            mergedList = mergedList.next

        # Find the one that is remaining / might be both empty
        rest = list1 if list2 == None else list2

        # Save the rest at the end of the list
        while rest:
            mergedList.next = rest
            rest = rest.next
            mergedList = mergedList.next
        
        return start.next
