# Solution 1( Brute Force) but this would result in time limit exceed error if applied on larger test cases.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dictionary={}
        listterm=[]
        winend, winstart=0,0
        for winend in range(0, len(nums)):
            sum, S=0, -10

            i=winend
            while i<len(nums):
                sum+=nums[i]
                listterm.append(sum)
                S=max(S, sum)
                i+=1
        return max(listterm)
      

      
#Solution2 -> Using Kedane Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum=nums[0]
        CurrSum=MaxSum
        for i in range(1, len(nums)):
            CurrSum=max(nums[i]+CurrSum, nums[i])
            MaxSum=max(MaxSum, CurrSum)
        return MaxSum

