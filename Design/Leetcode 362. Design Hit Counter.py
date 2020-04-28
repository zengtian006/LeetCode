class HitCounter:

    def __init__(self):
        self.times = [0]*300
        self.counts = [0]*300
        

    def hit(self, timestamp: int) -> None:
        t = timestamp % 300
        if self.times[t] != timestamp:
            self.times[t] = timestamp
            self.counts[t] = 1
        else:
            self.counts[t] += 1
        

    def getHits(self, timestamp: int) -> int:
        count = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                count += self.counts[i]
        return count