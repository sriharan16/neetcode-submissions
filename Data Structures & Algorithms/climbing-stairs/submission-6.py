class Solution:
    # s1  Bottom-up (tabulation) — the natural approach here

    # def climbStairs(self, n: int) -> int:
    #     if n <= 1: # base case
    #         return 1
    #     dp = [1] * (n+1)
    #     for i in range(2, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]
    
    # s2 Bottom-up (tabulation) — space opt
    def climbStairs(self, n: int) -> int:

        one, two = 1,1

        for i in range(2, n+1):
            temp = one
            one = one + two
            two = temp
        return one
