from typing import List


# Find first or Last occurence of number in sorted array
def findOccurrence(arr:List[int], target, f_o_l):
    print("Find ",f_o_l," occurrence of ",target)
    low = 0
    high = len(arr)-1
    first = -1
    last = -1
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid]==target:
            if f_o_l == "first":
                first = mid
                high = mid-1
            if f_o_l == "last":
                last = mid
                low = mid+1
        elif arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
    
    if f_o_l == "first":
        return first
    if f_o_l == "last":
        return last

# Driver Code
print("Find occurrence of: ")
array = [1,3,5,5,5,6,7,7,7,8,9,9]
print(findOccurrence(array,9,"last"))
