from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cur_gas = 0
        start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            cur_gas += g - c
            if cur_gas < 0:
                cur_gas = 0
                start = i + 1
        return start


print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
