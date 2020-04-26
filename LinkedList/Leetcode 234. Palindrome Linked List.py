class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        while head:
            if stack.pop()!=head.val:
                return False
            head = head.next
        return True