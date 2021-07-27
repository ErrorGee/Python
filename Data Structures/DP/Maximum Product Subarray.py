class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MaxProduct=max(nums)
        CurrentMax, CurrentMin=1,1
        for i in nums:
            CurrM=CurrentMax*i
            CurrentMax=max(CurrentMax*i, CurrentMin*i, i)
            CurrentMin=min(CurrentMin*i, CurrM, i)
            MaxProduct=max(MaxProduct, CurrentMax)
        return MaxProduct
        
