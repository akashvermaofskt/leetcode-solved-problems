# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode()
        current = start
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    current.next = ListNode(val=l1.val)
                    current = current.next
                    l1 = l1.next
                else:
                    current.next = ListNode(val=l2.val)
                    current = current.next
                    l2 = l2.next
            elif l1:
                current.next = ListNode(val=l1.val)
                current = current.next
                l1 = l1.next
            elif l2:
                current.next = ListNode(val=l2.val)
                current = current.next
                l2 = l2.next
            else:
                break
        return start.next
