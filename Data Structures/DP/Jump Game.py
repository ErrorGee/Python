class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #backtracking
        n=len(nums)
        FinalIndex=n-1
        for i in range(n-1, -1,-1):
            if i+nums[i]>=FinalIndex:
                FinalIndex=i
        return FinalIndex==0
