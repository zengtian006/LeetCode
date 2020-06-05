def sortedInsert(head, data):
    cur = head
    pre = None
    while cur and cur.data<=data:
        pre = cur
        cur = cur.next
    node = DoublyLinkedListNode(data)
    if cur == head:
        node.next = cur
        cur.prev = node
        return node
    elif not cur:
        pre.next= node
        node.prev = pre
        return head
    else:
        node.prev = cur.prev
        node.next = cur
        cur.prev.next= node
        cur.prev = node
        return head

# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem