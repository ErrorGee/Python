class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        Row=len(grid)
        Col=len(grid[0])
        dp=[[0 for j in range(Col)] for i in range(Row)]
        for i in range(Row):
            for j in range(Col):
                if i>0 and j>0:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j]=grid[i][j]+max(0 if i==0 else dp[i-1][j], 0 if j==0 else dp[i][j-1])
        # print(dp)
        return dp[Row-1][Col-1]
