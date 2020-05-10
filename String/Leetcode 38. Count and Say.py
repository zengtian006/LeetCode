class Solution:
    def countAndSay(self, n: int) -> str:
        i,res = 1, '1'
        while i<n:
            l, count = res[0], 0
            temp = ""
            for j in res:
                if j == l:
                    count+=1
                else:
                    temp += str(count)+l
                    l = j
                    count = 1
            temp += str(count)+l
            res = temp
            i+=1
        return res