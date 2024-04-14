
//Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    var mergedList = new ListNode();
    var start = mergedList;

    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            mergedList.next = list1;
            list1 = list1.next;
        }
        else {
            mergedList.next = list2;
            list2 = list2.next;
        }

        mergedList = mergedList.next;
    }

    var rest = list2 === null ? list1 : list2;

    while (rest !== null) {
        mergedList.next = rest;
        rest = rest.next;
        mergedList = mergedList.next;
    }
    
    return start.next;
};