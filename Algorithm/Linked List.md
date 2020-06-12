# Linked List

## 单向列表

1. 翻转列表

[Leetcode 206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
[Leetcode 25 Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

```python
    def reverseList(self, head:ListNode):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre

            # 两个指针同时往前走
            pre = cur
            cur = cur.next
        return pre
```

2. 快慢指针

取链表中点

```python
    def getMiddle(self, head: ListNode):
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next.next

```


## 双向链表(Double Linked List)

[Leetcode 146. LRU Cache](https://leetcode.com/problems/lru-cache/)
[Leetcode 460. LFU Cache](https://leetcode.com/problems/lfu-cache/)


基础操作

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.count = 0

    def appendToLast(self, node):
        node.next = self.tail
        node.pre = self.tail.pre
        self.tail.pre.next = node
        self.tail.pre = node
        self.count += 1
    
    def insertToFirst(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        self.count += 1

    def remove(self, node):
        pre, nxt = node.pre, node.next
        pre.next= nxt
        nxt.pre = pre
        self.count -= 1

```