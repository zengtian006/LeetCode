class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic = {}
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        pos = 1
        while fast and fast not in dic:
            slow = slow.next
            fast = fast.next
            dic[slow] = pos
            pos += 1

        return fast