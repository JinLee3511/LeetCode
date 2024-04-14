
// Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}
 
class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        var mergedList = ListNode()
        var start = mergedList

        guard var list1 = list1 else { return list2 }
        guard var list2 = list2 else { return list1 }

        var breakLoop = false
        var list1Empty = false

        while (!breakLoop) {
            if list1.val <= list2.val {
                mergedList.next = list1
                if let list1Next = list1.next {
                    list1 = list1Next
                }
                else {
                    breakLoop = true
                    list1Empty = true
                }
            }
            else {
                mergedList.next = list2
                if let list2Next = list2.next {
                    list2 = list2Next
                }
                else {
                    breakLoop = true
                }
            }
            
            if let next = mergedList.next {
                mergedList = next
            }
        }

        var rest = list1Empty ? list2 : list1
        breakLoop = false

        while (!breakLoop) {
            mergedList.next = rest
            if let restNext = rest.next {
                rest = restNext
            }
            else {
                breakLoop = true
            }
            if let next = mergedList.next {
                mergedList = next
            }
        }

        return start.next
    }
}