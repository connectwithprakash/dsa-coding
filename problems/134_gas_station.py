class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n_pass = 0
        step = -1
        total_gas = 0
        n = len(gas)
        max_step = 2*n
        start_pos = None

        while (step < max_step):
            step += 1
            idx = step % n
            total_gas += (gas[idx] - cost[idx])
            if total_gas < 0:
                start_pos = None
                total_gas = 0
                n_pass = 0
            else:
                if start_pos is None:
                    start_pos = idx
                n_pass += 1

            if n_pass == n:
                return start_pos

