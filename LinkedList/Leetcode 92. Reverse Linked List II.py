class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            pre = pre.next
        cur = pre.next
        for _ in range(m,n):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return dummy.next