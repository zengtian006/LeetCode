class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.pre = None

class Dll:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.count = 0
        
    def insertToHead(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        self.count += 1
    
    def remove(self, node):
        pre, nxt = node.pre, node.next
        pre.next = nxt
        nxt.pre = pre
        self.count -= 1
        
    def removeLast(self):
        if self.count == 0:
            return 
        last = self.tail.pre
        self.remove(last)
        return last
    
    
class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.dic = {}
        self.freq_dic = collections.defaultdict(Dll)
        self.min_freq = 0
        
    def update(self, node):
        freq = node.freq
        self.freq_dic[freq].remove(node)
        if self.min_freq == freq and self.freq_dic[freq].count == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_dic[node.freq].insertToHead(node)
        
        
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.update(node)
            return node.val
        return -1
            
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return                                    
        if key not in self.dic:
            if self.size == self.cap:
                node = self.freq_dic[self.min_freq].removeLast()
                del self.dic[node.key]
                self.size -= 1
                
            node = Node(key, value)
            self.dic[key] = node
            self.freq_dic[1].insertToHead(node)
            self.min_freq = 1
            self.size += 1
        else:
            node = self.dic[key]
            self.update(node)
            node.val = value