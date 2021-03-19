from typing import List

# Binary Search Iterative
def binarySearchIterative(array:List[int], target)->int:
    low =0
    high = len(array)-1

    while low<=high:
        mid = low+(high-low)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return -1

# Binary Search Recursive
def binarySearchRecursive(array:List[int], low, high, target)->int:
    if low > high:
        return -1
    mid = low+(high-low)//2
    if array[mid] == target:
        return mid
    if array[mid] < target:
        return binarySearchRecursive(array,mid+1,high,target)
    else:
        return binarySearchRecursive(array,low,mid-1,target)

# Binary Search Rotated Sorted array - Find how many times the array is rotated.
def binarySearchRotatedArray(array:List[int])->int:
    low = 0
    high = len(array)-1

    while low <= high:
        mid = low + (high-low)//2
        if array[low] <= array[mid] and array[mid]<= array[high]:
            return low
        prev = array[(mid-1+len(array))%(len(array))]
        next = array[(mid+1)%(len(array))]
        if prev >= array[mid] and next >= array[mid]:
            return mid
        elif array[mid]<=array[high]:
            high = mid-1
        elif array[mid]>=array[low]:
            low = mid+1
    return -1

# Binary Search Rotated Sorted Array - Find how many times the array is rotated - Recursive
def binarySearchRotatedArrayRecursive(array:List[int],low,high)->int:
    if low>high:
        return -1
    mid = low + (high-low)//2
    if array[low] <= array[mid] and array[mid]<=array[high]:
        return low
    prev = array[(mid-1+len(array))%(len(array))]
    next = array[(mid+1)%(len(array))]
    if array[mid]<=prev and array[mid]<=next:
        return mid
    elif array[mid]<array[high]:
        high = mid-1
        return binarySearchRotatedArrayRecursive(array,low,high)
    elif array[mid]>array[low]:
        low =mid+1
        return binarySearchRotatedArrayRecursive(array,low,high)


# Driver Code
array = [-10,-4,-2,-1,1,8,9,10,18]
print("Binary Search Iterative: ")
print(binarySearchIterative(array,7))
print("Binary Search Recursive: ")
print(binarySearchRecursive(array,0,len(array)-1,7))

#array = [-2,-1,1,8,9,10,18,-10,-4]
array = [10,18,-10,-4,-2,-1,1,8,9]
print("Binary Search Rotated Array: ")
print(binarySearchRotatedArray(array))

print("Binary Search Rotated Array Recursive: ")
print(binarySearchRotatedArrayRecursive(array,0,len(array)-1))