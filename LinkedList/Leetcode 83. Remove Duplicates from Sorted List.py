class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val :
                start = cur
                while start.next and start.val == start.next.val :
                    start = start.next
                cur.next = start.next
            cur = cur.next
        return head