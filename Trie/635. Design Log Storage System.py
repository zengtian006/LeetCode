class Dir:
    def __init__(self):
        self.child = collections.defaultdict(Dir)
        self.id = -1
        self.isFile = False
        self.t = 0
        
class LogSystem:
    graDic = {'Year':0, 'Month':1, 'Day':2, 'Hour':3, 'Minute':4, 'Second':5}

    def __init__(self):
        self.d = Dir()

    def put(self, id: int, timestamp: str) -> None:
        cur = self.d
        timestamp = timestamp.split(':')
        for i in range(len(timestamp)):  
            cur = cur.child[timestamp[i]]
            cur.t =int("".join(timestamp[:i+1]))
        cur.id = id
        cur.isFile = True

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        cur = self.d
        level = LogSystem.graDic[gra]

        s = s.split(':')
        e = e.split(':')
        
        q = collections.deque()
        q.append(cur)
        i = 0
        res = []
        while q:
            size = len(q)
            for _ in range(size):
                dd = q.popleft()
                if dd.isFile:
                    res.append(dd.id)
                    continue
                for ch in dd.child:
                    if level >= 0:
                        if int("".join(s[:i+1]))<=dd.child[ch].t<=int("".join(e[:i+1])):
                            q.append(dd.child[ch])
                    else:
                        q.append(dd.child[ch])
            level -= 1
            i+=1
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)