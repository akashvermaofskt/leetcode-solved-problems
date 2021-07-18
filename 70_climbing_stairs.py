class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [None] * n
        self.n = n
        return self.solve(self, 0)

    def solve(self, i):
        if i > self.n:
            return 0
        if i == self.n:
            return 1
        if self.dp[i]:
            return self.dp[i]
        self.dp[i] = self.solve(self, i + 1) + self.solve(self, i + 2)
        return self.dp[i]


print(Solution.climbStairs(Solution, 2))
