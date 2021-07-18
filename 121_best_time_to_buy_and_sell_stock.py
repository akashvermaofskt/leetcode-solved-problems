from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = prices[-1]
        ans = 0
        i = len(prices) - 2
        while i >= 0:
            ans = max(ans, max_so_far - prices[i])
            max_so_far = max(max_so_far, prices[i])
            i = i - 1
        return ans


print(Solution.maxProfit(Solution, [1,2]))
