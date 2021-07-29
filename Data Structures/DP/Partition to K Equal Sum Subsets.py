class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:   
        def findIf(CurrSum,k,index):
            if k==0:
                return True
            if CurrSum==Target:
                return findIf(0, k-1, 0)
            for i in range(index, n):
                if not Visited[i] and CurrSum+nums[i]<=Target:
                    Visited[i]=True
                    if findIf(CurrSum+nums[i], k, i+1):
                        return True
                    Visited[i]=False
            return False
        if sum(nums)%k!=0:
            return False
        else:
            n=len(nums)
            Target=sum(nums)//k
            Visited=[False]*(n)
            ans=findIf(0, k,0)
            return ans
 #problems i faced---->when i did not  use index, it gve me a time limit exceeded error reson being, it was iterating from the start again and again
