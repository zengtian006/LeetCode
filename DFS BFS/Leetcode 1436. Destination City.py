class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = collections.defaultdict(list)
        for [x,y] in paths:
            dic[x].append(y)
           
        res = set()    
        stack = []
        stack.append(paths[0][0])
        while stack:
            while dic[stack[-1]]:
                stack.append(dic[stack[-1]].pop())
            return stack[-1]