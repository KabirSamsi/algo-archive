def minhelper(nums, left, right):
    #If the left is greater, then we pivot the wraparound here, so we have found the mid
    #If the right is greater and the left is less, than we don't know anything yet. Recurse through both
    #If both are less, then we know that the pivot must be to the right
    
    if right-left == 2:
        return min(nums[left], nums[left+1])
    if right-left == 1:
        return nums[left]
    
    mid = left + (right-left)// 2
    print(left, right, mid)

    if nums[mid-1] > nums[mid]:
        return nums[mid]
    
    if nums[mid+1] < nums[mid]:
        return nums[mid+1]

    if nums[mid-1] < nums[mid] and nums[mid+1] > nums[mid]:
        return min(minhelper(nums, left, mid), minhelper(nums, mid+1, right))

def findMin(nums):
    return minhelper(nums, 0, len(nums))

    


print(findMin([3,4,5,6,7,1,2]))