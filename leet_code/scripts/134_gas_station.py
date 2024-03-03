class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            start_pos, total_gas = 0, 0
            for idx in range(len(gas)):
                total_gas += (gas[idx] - cost[idx])
                if total_gas < 0:
                    start_pos, total_gas = idx + 1, 0
            return start_pos

