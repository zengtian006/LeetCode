class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        count = (len(stack)-1)//2
        cur = head
        while count>0:
            node = stack.pop()
            nxt = cur.next
            cur.next = node
            node.next = nxt
            cur = nxt
            count-=1
        stack[-1].next = None