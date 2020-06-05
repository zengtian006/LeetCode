class Solution:
    def maximumSwap(self, num: int) -> int:
        i = 1
        num = list(str(num))
        dic = {}
        for i in range(len(num)):
            dic[int(num[i])] = i
            
        for i in range(len(num)):
            for j in range(9, int(num[i]), -1):
                if j in dic and dic[j]>i:
                    num[i], num[dic[j]] = num[dic[j]], num[i]
                    return int("".join(num))
        return int("".join(num))