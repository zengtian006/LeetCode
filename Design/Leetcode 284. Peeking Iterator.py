class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.nxt = self.iter.next() if self.iter.hasNext() else None
        

    def peek(self):
        return self.nxt
        

    def next(self):
        res = self.nxt
        self.nxt = self.iter.next() if self.iter.hasNext() else None
        return res
        

    def hasNext(self):
        return self.nxt != None