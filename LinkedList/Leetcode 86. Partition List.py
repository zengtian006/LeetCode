class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0)
        pre = dummy 
        dummy.next = head
        # find the last node Y which is smaller than x
        while pre.next and pre.next.val<x:
            pre = pre.next  
        cur = pre
        while cur.next:
            if cur.next.val >= x:
                cur = cur.next
            else:
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                pre = pre.next
        return dummy.next