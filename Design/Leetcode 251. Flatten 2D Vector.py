class Vector2D:

    def __init__(self, v: List[List[int]]):
        self. v = v
        self.inner = 0
        self.outer = 0

    def next(self) -> int:
        while self.outer < len(self.v) and self.inner == len(self.v[self.outer]) :
            self.inner = 0
            self.outer +=1
        res = self.v[self.outer][self.inner]
        self.inner += 1
        return res

    def hasNext(self) -> bool:
        while self.outer < len(self.v) and self.inner == len(self.v[self.outer]) :
            self.inner = 0
            self.outer +=1
        return self.outer < len(self.v)