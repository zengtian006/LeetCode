class Logger:

    def __init__(self):
        self.times = [0]*10
        self.dic = collections.defaultdict(set)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        t = timestamp % 10
        if self.times[t] != timestamp:
            self.times[t] = timestamp  # reset
            self.dic[t] = set() #reset
        for i in range(10):
            if timestamp - self.times[i] < 10:
                if message in self.dic[i]:
                    return False
        self.dic[t].add(message)
        return True