class Solution:
    def maxSubArray(self, nums: list) -> int:
        ans = -1000000
        max_ans = ans
        for n in nums:
            ans = max(ans + n, n)
            max_ans = max(ans, max_ans)
        return max_ans


print(Solution.maxSubArray(Solution, [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
