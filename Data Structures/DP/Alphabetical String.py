# A string is given, you have to find the number of deletions that must be made to trun it into an alphabetical string
#Alphabetical strings are those strings which are like this -> "abcdefghijklmnopqrstuvwxyz"
# You have to check how many insertions(minimum) you have to do in the given string so that the inpput strings looks like the given string 
def LCS(String1, String2, n, m, dp):
    if m==0 or n==0:
        return 0
    if dp[n][m]!=-1:
        return dp[n][m]
    if String1[n-1]==String2[m-1]:
        dp[n][m]=1+LCS(String1, String2, n-1, m-1, dp)
        return dp[n][m]
    dp[n][m]=max(LCS(String1, String2, n, m-1, dp),
     LCS(String1, String2, n-1, m, dp))
    return dp[n][m]

if __name__=="__main__":
    st1="abcdefghijklmnopqrstuvwxyz"
    st2="ijklmnopqrstuvwxyzabcdefgh"
    n=len(st1)
    m=len(st2)
    dp=[[-1 for j in range(m+1)] for i in range(n+1)]
    res=26-LCS(st1, st2, n, m, dp)
    print(res)
