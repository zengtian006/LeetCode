class Solution:
    def canCross(self, stones: List[int]) -> bool:
        fail = set()
        stone_set = set(stones)
        stack = []
        stack.append((0,0))
        while stack:
            cur_pos, jump = stack.pop()
            for j in (jump-1, jump, jump+1):
                pos = cur_pos+j
                if pos > 0 and pos in stone_set and (pos, j) not in fail:
                    if pos == stones[-1]:
                        return True
                    stack.append((pos, j))
            
            fail.add((cur_pos, jump))
        return False