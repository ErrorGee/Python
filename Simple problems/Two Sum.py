# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            index=[]
            for j in range(i+1, len(nums)):
                Subtract=target-nums[i]
                if Subtract==nums[j]:
                    index.append(i)
                    index.append(j)
                    return index
                  
#using Hashmap-->Dictionary in Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i in range(0, len(nums)):
            Output=[0]*2
            Subtract=target-nums[i]
            if Subtract in index.keys():
                Output[0]=index.get(Subtract)
                Output[1]=i
                return Output
            index[nums[i]]=i
            
#Using 2 Pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        WinStart, WinEnd, WinSum=0,0,0
        for WinStart in range(0, len(nums)):
            WinEnd=WinStart+1
            list1=[0]*2
            while WinEnd<len(nums):
                WinSum=nums[WinStart]
                WinSum+=nums[WinEnd]
                if WinSum==target:
                    list1[0]=WinStart
                    list1[1]=WinEnd
                    return list1
                WinEnd+=1
        return 0
            
