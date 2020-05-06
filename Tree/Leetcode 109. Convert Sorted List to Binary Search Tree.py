class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        pre = None
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        root = TreeNode(slow.val)
        if slow == head:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root