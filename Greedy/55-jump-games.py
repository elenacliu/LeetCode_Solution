class Solution:
    # @lru_cache(None)
    def canJump(self, nums: List[int]) -> bool:
        # 法1：动态规划，O(n^3)
        # 从最后一个元素开始向前找
        # dp[i][j]代表能不能从i跳跃到j
        # dp[i][j] = true if i < j and j <= to[i]
        # dp[0][n-1] = dp[0][k] & dp[k][n-1] for k in range(1, n-1)
        # dp[i][j] = dp[i][k] & dp[k][j] for k in range(i+1, j)
        # O(n^3)

        # 法2：递归
        # @lru_cache
        # 针对第一个可以到达的位置进行递归
        n = len(nums)
        if n <= 1:
            return True
        
        # maxlen = min(n, nums[0] + 1)
        # for i in range(maxlen):
        #     if self.canJump(nums[1:]):
        #         return True
        # return False

        # 法3：由递归想到的动态规划
        # O(n^2)
        # dp[i]代表着可以从i跳到终点
        # dp[i] = dp[j] for i < j <= i + nums[i]
        # 还是超时
        # dp = [False] * n
        # dp[n - 1] = True
        # for i in range(n-2,-1,-1):
        #     maxlen = min(n, nums[i] + i + 1)
        #     for j in range(maxlen - 1, i, -1):
        #         if dp[j]:
        #             dp[i] = True
        #             break
            
        # return dp[0]

        # 法4：单次遍历
        maxpos = 0
        for i in range(n):
            if i <= maxpos:
                maxpos = max(maxpos, nums[i] + i)
                if maxpos >= n - 1:
                    return True
        
        return False
