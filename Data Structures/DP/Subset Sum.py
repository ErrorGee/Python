def subsetSum(arr, sum, n, dp):
    if (sum==0):
        return True
    if (n==0):
        return False
    if dp[n][sum]!=False:
        return dp[n][sum]
    if arr[n-1]>sum:
        dp[n][sum]=subsetSum(arr, sum, n-1, dp)
        return dp[n][sum]
    dp[n][sum]=subsetSum(arr, sum-arr[n-1], n-1, dp) or subsetSum(arr, sum, n-1, dp)
    return dp[n][sum]
if __name__=="__main__":
    arr=[1,2,3,4,5]
    SUM=78
    n=len(arr)
    dp=[[False for j in range(SUM+1)] for i in range(n+1)]
    ans=subsetSum(arr, SUM, n, dp)
    print(ans)
