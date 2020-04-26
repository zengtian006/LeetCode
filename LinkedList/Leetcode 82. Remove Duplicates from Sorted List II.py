class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            nxt = cur.next.next
            if nxt and cur.next.val == nxt.val:
                while nxt and cur.next.val == nxt.val:
                    nxt = nxt.next
                cur.next = nxt
            else:
                cur = cur.next
        return dummy.next