
# 147 =>True
# 从第0位开始
# 走一步到 4
# 走四步到 7
# 走七步到 0
# 每一位都要访问到，并且最终回归到第0位

class Solution:
    def reverse(self, x: int) -> int:
        
        def check(x):
            visited = set()
            x = str(x)
            if len(x) == 1:
                return True
            s = int(x[0])
            s %= len(x)
            visited.add(s)
            while s!=0 and s<len(x):
                s += int(x[s])
                s %= len(x)
                if s in visited:
                    return False
                visited.add(s)
                if s == 0 and len(visited) == len(x):
                    return True
                if len(visited) < len(x) and s==0:
                    return False
                
            return False
        res = []
        for num in range(100,500):
            dic = {}
            dup = False
            for char in str(num):
                if char in dic:
                    dup = True
                    break
                dic[char] = 1
            if dup:
                continue
                    
            if check(1):
                res.append(num)
        return res
