class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 本质上和零钱兑换没有区别，首先找到和的一半是多少，然后再找组合情况
        # 没有必要排序
        # P.S. 01背包的计数问题
        # 状态：dp[i][j] 代表 nums[1...i] 是否可能抽出一些数和为j
        # 转移方程：dp[i][j] = dp[i-1][j - num] | dp[i-1][j] -> dp[j] = dp[j-num] | dp[j]
        # 初始化：当i=0时，j=0时肯定为True, 但是当j=1...s时，肯定是False
        # 遍历次序：由于是01背包问题，因此内层循环只能逆序遍历
        s = sum(nums)
        if s % 2:
            return False
        s = s // 2
        
        dp = [False for _ in range(s+1)]
        dp[0] = True
        
        for num in nums:
            for i in range(s, num-1, -1):
                dp[i] = dp[i - num] | dp[i]
        
        return dp[s]          
            