class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;
        if(n == 0)
            return 0;
        int[][] dp = new int[n+2][n+2];
        int[] points = new int[n+2];
        points[0] = points[n+1] = 1;
        for(int i = 1; i <= n; i++)
            points[i] = nums[i-1];
        for(int i = n; i >= 0; i--)
            for(int j = i+1; j <= n+1; j++)
                for(int k = i+1; k < j; k++) {
                    dp[i][j] = Math.max(dp[i][k]+dp[k][j]+points[i]*points[k]*points[j], dp[i][j]);
                }
        return dp[0][n+1];
    }
}
