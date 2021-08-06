import math
def jumpPos(arr, x, n):
    step=math.sqrt(n)
    prev=0
    while arr[int(min(step, n))]<x:
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
    while arr[int(prev)]<x:
        prev+=1
        if prev==min(step, n):
            return -1
    if arr[int(prev)]==x:
        return int(prev)
    return -1

if __name__=="__main__":
    arr=[2,12,23,45,55,67,68,90,189,190,200,201]
    x=55
    n=len(arr)
    ans=jumpPos(arr, x, n)
    print(ans)

    #time Complexity--->O(root(n))
    #space complexity is O(n)
    #After jumping appropriate steps, it does somelinear search
    #hence the time complexity lies between the time complexity of linear Search(--> O(n)) 
    # and the time complexity of Binary Search(--> O(log n))
    #Binary search is still better than Jump search but in some cases, Jump search can turn out to be effective
