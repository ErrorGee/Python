class Solution:
    def longestValidParentheses(self, s: str) -> int:
        String=s
        dp=[0 for x in String]
        for i in range(len(String)):
            if String[i]=="(":
                pass
            if String[i]==")":
                if i-1<0:
                    continue
                if String[i-1]=="(":
                    dp[i]=dp[i-2]+2
                    continue
                if i-dp[i-1]-1<0:
                    continue
                if String[i-dp[i-1]-1]=="(":
                    dp[i]=dp[i-1]+2 +dp[i-dp[i-1]-2]
        if len(dp)==0:
            return 0
        return max(dp)
                    
        
            
