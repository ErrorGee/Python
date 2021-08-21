def tabularLcs(st1, st2,m,n, dp):
    for i in range(1,m+1):
        for j in range(1, n+1):
            if st1[i-1]==st2[j-1]:
                dp[i][j]=dp[i-1][j-1]+st1[i-1]
            else:
                if len(dp[i-1][j])>len(dp[i][j-1]):
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i][j-1]
    #print(dp[m][n])
    return dp[m][n]         
if __name__=="__main__":
    str1=input()
    str2=input()
    m=len(str1)
    n=len(str2)
    dp=[["" for j in range(n+1)] for i in range(m+1)]
    LCS=tabularLcs(str1, str2, m, n, dp)
    p1, p2=0,0
    ans=''
    for character in LCS:
        while str1[p1]!=character:
            ans+=str1[p1]
            p1+=1
        while str2[p2]!=character:
            ans+=str2[p2]
            p2+=1
        ans+=character
        p1+=1
        p2+=1
    ans+= str1[p1:]+str2[p2:]
    print(ans)
                
            
        
