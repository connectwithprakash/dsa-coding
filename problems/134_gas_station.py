class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_pos = 0
        while start_pos < len(gas):
            total_gas = 0
            for idx in range(len(gas)+1):
                current_pos = (start_pos + idx) % len(gas)
                total_gas += gas[current_pos]
                if total_gas >= cost[current_pos]:
                    total_gas -= cost[current_pos]
                else:
                    break
            if (start_pos == current_pos) and (idx == len(gas)):
                return start_pos
            start_pos += 1
        return -1

