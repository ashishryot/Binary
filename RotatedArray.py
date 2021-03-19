from typing import List

# Smallest element in the rotated sorted array
def smallestElement(array:List[int])->int:
    low = 0
    high = len(array)-1

    while low <=high:
        mid =low+(high-low)//2
        if array[low]<=array[mid] and array[mid]<=array[high]:
            return low
        prev = (mid-1+len(array))%len(array)
        next = (mid+1)%len(array)
        if array[mid]<=array[prev] and array[mid]<=array[next]:
            return mid
        elif array[mid]<array[high]:
            high = mid-1
        elif array[mid]>array[low]:
            low=mid+1
    return -1

# Smallest element in the rotated sorted array with duplicate elements
def smallestElementwDuplicates(array:List[int])->int:
    low =0
    high = len(array)-1
    while low<=high:
        mid = low+(high-low)//2
        if array[low]<=array[mid] and array[mid]<=array[high]:
            return low
        prev = (mid-1+len(array))%len(array)
        next = (mid+1)%len(array)
        if array[mid]<=array[prev] and array[mid]<=array[next]:
            return mid
        elif array[mid]<=array[high]:
            high=mid-1
        elif array[mid]>=array[low]:
            low=mid+1
    return -1

#Driver Code
array = [17,20,-10,-10,-8,-5,-1,1,3,5,8,9,10,12]
print("Smallest Element in rotated array with no duplicates: ")
ind = smallestElement(array)
if ind == -1:
    print("Couldn't find lowest element due to technical issues. Working on a fix.")
else:
    print("smallest element is: ",array[ind])

print("smallest element in rotated array with duplicates present: ")
array = [17,20,-10,-10,-8,-5,-1,1,3,5,8,9,10,12]
ind = smallestElementwDuplicates(array)
if ind == -1:
    print("Couldn't find lowest element due to technical issues. Working on a fix.")
else:
    print("smallest element is: ",array[ind])