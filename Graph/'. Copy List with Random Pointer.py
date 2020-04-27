class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        new_head = dummy
        dic = {}
        while head:
            if head not in dic:
                dic[head] = Node(head.val)
            new_head.next = dic[head]
            if head.random:
                if head.random not in dic:
                    dic[head.random] = Node(head.random.val)
                new_head.next.random = dic[head.random]
            new_head = new_head.next
            head = head.next
        return dummy.next