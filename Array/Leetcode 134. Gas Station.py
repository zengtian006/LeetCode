class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = cur_gas = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
        return start if total >= 0 else -1

        #从第一个加油站开始，total是看从任意一点能不能回到原点，cur_gas是开从start出发，车上有多少汽油，如果cur_gar<0表示汽油不够，则start和汽油要重新计算