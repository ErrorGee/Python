#Brute Force   
class Solution:
    def trap(self, height: List[int]) -> int:
        def countRain(height, n, MaxRightArr, MaxLeftArr):
            Trap=0
            for i in range(1,n-1):
                # print(height[i])
                # print(MaxLeftArr, MaxRightArr)
                if height[i]<MaxLeftArr[i] and height[i]<MaxRightArr[i]:
                    Trap+=(min(MaxLeftArr[i],MaxRightArr[i])-height[i])*width
            return Trap                     
        n=len(height)
        if n>=3:
            width=1
            MaxLeftArr=[height[0]]*n
            MaxRightArr=[height[n-1]]*n
            leftmax,rightmax=MaxLeftArr[0], MaxRightArr[n-1]
            for i in range(1,n):
                if leftmax<height[i]:
                    MaxLeftArr[i]=leftmax
                    leftmax=height[i]
                else:
                    MaxLeftArr[i]=leftmax
            for j in range(n-1, 0,-1):
                if rightmax<height[j]:
                    MaxRightArr[j]=rightmax
                    rightmax=height[j]
                else:
                    MaxRightArr[j]=rightmax
            return countRain(height, n, MaxRightArr, MaxLeftArr)
        else:
            return 0
          
          
#using 2 Pointers         
class Solution:
    def trap(self, height: List[int]) -> int:
        def twoPointer(height,MaxRight, MaxLeft, Temp):
            left,right=1,n-1
            while left<=right:
                if MaxLeft<MaxRight:
                    if height[left]<MaxLeft and height[left]<MaxRight:
                        Temp+=min(MaxLeft,MaxRight)-height[left]
                    if height[left]>MaxLeft:
                        MaxLeft=height[left]
                    left+=1
                else:
                    if height[right]<MaxLeft and height[right]<MaxRight:
                        Temp+=min(MaxLeft, MaxRight)-height[right]
                    if height[right]>MaxRight:
                        MaxRight=height[right]
                    right-=1
            return Temp
        n=len(height)
        if n>=3:
            MaxLeft=height[0]
            MaxRight=height[n-1]
            Temp=0
            ans=twoPointer(height,MaxRight, MaxLeft, Temp)
            return ans
        else:
            return 0      
          
         
