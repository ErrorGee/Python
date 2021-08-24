class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        res=self.LCS(word1,word2, m, n, dp)
        MinStep=(len(word1)-res)+(len(word2)-res)
        return MinStep
        
    def LCS(self,word1,word2, m, n, dp):
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        # print(dp[m][n])
        return dp[m][n]

                
                    
        
