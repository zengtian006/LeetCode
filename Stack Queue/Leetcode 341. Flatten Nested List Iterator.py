import collections
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = collections.deque()
        self.flatten(nestedList)
    def flatten(self, nestedList):
        if not nestedList: return
        for ni in nestedList:
            if ni.isInteger():
                self.q.append(ni.getInteger())
            else:
                self.flatten(ni.getList())
    
    def next(self) -> int:
        if self.q:
            return self.q.popleft()
    
    def hasNext(self) -> bool:
        return len(self.q)>0