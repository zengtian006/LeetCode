class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre and pre.next:
            if pre.next and pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next