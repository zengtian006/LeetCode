class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        i = j = 0
        self.v = []
        while i< len(v1) and j < len(v2):
            self.v.append(v1[i])
            self.v.append(v2[j])
            i+=1
            j+=1
        if i < len(v1):
            self.v.extend(v1[i:])    
        if j < len(v2):
            self.v.extend(v2[j:])
        self.p = 0
    def next(self) -> int:
        val = self.v[self.p]
        self.p+=1
        return val
    def hasNext(self) -> bool:
        if self.p >= len(self.v):
            return False
        return True