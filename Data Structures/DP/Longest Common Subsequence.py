def longestCommonSubstring(String1, String2, m,n,dp):
    if m==0 or n==0:
        return 0
    
    if dp[m][n]!=-1:
        return dp[m][n]
    if String1[m-1]==String2[n-1]:
        dp[m][n] =1+ longestCommonSubstring(String1, String2, m-1,n-1,dp)
        return dp[m][n]
    dp[m][n]= max(longestCommonSubstring(String1, String2, m-1,n,dp), 
                longestCommonSubstring(String1, String2, m,n-1,dp))
    return dp[m][n]

if __name__=="__main__":
    String1=input()
    String2=input()
    # rev=String1[::-1]
    # print(rev)
    # String2=rev
    dp=[[-1 for j in range(len(String2)+1)] for i in range(len(String1)+1)]
    
    Longest=longestCommonSubstring(String1, String2, len(String1), len(String2),dp)
    print(Longest)
    

#the palindrome problem is avaliable on leetcode
#plindrome subsequence
#only diff. is to reverse the original string in the main fxn
if __name__=="__main__":
    String1=input()
    rev=String1[::-1]
    String2=rev
    dp=[[-1 for j in range(len(String2)+1)] for i in range(len(String1)+1)]
    
    Longest=longestCommonSubstring(String1, String2, len(String1), len(String2),dp)
    print(Longest)

    
