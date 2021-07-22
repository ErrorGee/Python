#Linear Search in python...............................................................................................................................
def LinearSearch(array, num, len):
    for i in range(0,len):
        if num==array[i]:
            return i
    return -1

array=list(map(int, input().split(",")))
num=int(input())
result=LinearSearch(array, num, len(array))
if result>=0:
    print("{} present at position {}".format(num, result+1))
else:
    print("Element not found")

#Linear search Ends......................................................................................................................................


#Binary Search in Python..................................................................................................................................
def BinarySearch(arr, first, last, num):
    if first<=last:
        mid=(first+last)//2
        mid=low+(high-low)//2
        if arr[mid]==num:
            return mid
        if arr[mid]>num:
            return BinarySearch(arr, first, mid-1, num)
        return BinarySearch(arr, mid+1, last, num)
    return -1
SortedArray=list(map(int, input().split(",")))
num=int(input())
first, last=0,len(SortedArray)-1
result=BinarySearch(SortedArray, first, last, num)
if result>=0:
    print("{} found at position {}".format(num,result+1))
else:
    print("element not found")

#Binary Search Ends Here...................................................................................................................................
