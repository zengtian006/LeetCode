class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        left, right = 0, 255
        while count[left]==0:
            left += 1
        while count[right]==0:
            right -= 1
        min_n = left
        max_n = right
        counts = 0
        sums = 0
        mode = 0
        for i in range(left, right+1):
            if count[i]>0:
                counts += count[i]
                sums += i*count[i]
                if count[i]>count[mode]:
                    mode = i
        mean = sums/counts
        
        m1 = m2 = 0
        if counts % 2 == 0:
            m1 = counts//2
            m2 = counts//2+1
        else:
            m1 = m2 = (counts+1)//2
           
        cnt = 0
        for i in range(left, right+1):
            if (cnt<m1 and count[i]+cnt>=m1):
                m1 = i
            if (cnt<m2 and count[i]+cnt>=m2):
                m2 = i
                break
            cnt += count[i]
        median = (m1+m2)/2
        return [min_n, max_n,mean, median,mode]