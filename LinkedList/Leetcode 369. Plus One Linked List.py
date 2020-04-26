class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        carry = self.dfs(head)
        if carry == 1:
            root = ListNode(1)
            root.next = head
            return root
        else:
            return head
    
    def dfs(self, node):
        if not node:
            return 1
        carry = self.dfs(node.next)
        sums = node.val + carry
        node.val = sums%10
        return sums//10