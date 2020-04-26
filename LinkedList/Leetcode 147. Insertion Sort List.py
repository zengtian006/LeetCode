class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            if cur.next.val > cur.val:
                cur = cur.next
            else:
                nxt = cur.next
                cur.next = nxt.next
                pre = dummy
                while pre.next and pre.next.val<nxt.val:
                    pre = pre.next
                nxt.next = pre.next
                pre.next = nxt
        return dummy.next