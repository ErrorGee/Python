def Tabulardp(st1, st2,n,m, dp):
    for i in range(1,n+1):
        for j in range(1, m+1):
            if st1[i-1]==st2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]
if __name__=="__main__":
    st1=input()
    st2=input()
    dp=[[0 for j in range(len(st2)+1)] for i in range(len(st1)+1)]
    ans=Tabulardp(st1, st2, len(st1), len(st2), dp)
    print(ans)
