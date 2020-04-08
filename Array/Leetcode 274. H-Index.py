class Solution:
    def hIndex(self, citations: List[int]) -> int:
        dic = {}
        for i in range(len(citations)):
            if citations[i] > len(citations):
                dic[len(citations)] = dic.get(len(citations),0)+1
            else:
                dic[citations[i]] = dic.get(citations[i],0)+1
                
        count = 0
        for i in range(len(citations),-1,-1):
            count += dic.get(i,0)
            if count>=i:
                return i  
        return 0