"""
Input: Matrix of person's wealth (money across different banks)
Output: Total wealth of the person with the maximum wealth
Idea: One way to do it would be to loop through each row and store the maximum wealth in a temporary variable
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for idx in range(len(accounts)):
            person_idx_wealth = 0

            for jdx in range(len(accounts[0])):
                person_idx_wealth += accounts[idx][jdx]

            if person_idx_wealth > max_wealth:
                max_wealth = person_idx_wealth

        return max_wealth
