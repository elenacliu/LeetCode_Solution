class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        if(m == 0)
            return 0;
        int n = dungeon[0].length;
        if(n == 0)
            return 0;
        int[][] dp = new int[m+1][n+1];
        for (int i = 0; i <= m; i++)
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        dp[m][n-1] = dp[m-1][n] = 1;
        for(int i = m - 1; i >= 0; --i)
            for(int j = n - 1; j >= 0; --j) {
                int minn = Math.min(dp[i+1][j], dp[i][j+1]);
                dp[i][j] = Math.max(minn - dungeon[i][j], 1);
            }
        return dp[0][0];
    }
}
