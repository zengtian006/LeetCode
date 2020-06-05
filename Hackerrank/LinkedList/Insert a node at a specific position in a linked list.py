def insertNodeAtPosition(head, data, position):
    pre = None
    cur = head
    while cur and position!=0:
        pre = cur
        cur = cur.next
        position -= 1
    node = SinglyLinkedListNode(data)
    if not cur:
        pre.next = node
    else:
        node.next = cur
        pre.next = node
    return head

# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem