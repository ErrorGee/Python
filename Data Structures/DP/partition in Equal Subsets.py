class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        else:
            Sum=sum(nums)//2
            dp=set()
            dp.add(0)
            n=len(nums)
            for i in range(n-1, -1,-1):
                newdp=set()
                for j in dp:
                    if j+nums[i]==Sum:
                        return True
                    newdp.add(j+nums[i])
                    newdp.add(j)
                dp=newdp
            
            return True if Sum in dp else False
