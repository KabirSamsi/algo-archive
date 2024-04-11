class Solution(object):
    def binsearch(self, nums, target, left, right):
        if right==left:
            if nums[left] == target or nums[left] > target:
                return left
            return right+1
        
        mid = (left+right) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return self.binsearch(nums, target, mid+1, len(nums)-1)
        return self.binsearch(nums, target, left, mid)

    def searchInsert(self, nums, target):
        return self.binsearch(nums, target, 0, len(nums)-1)
            

        #Find halfway point
        #Recursively divide and search
        #If not in specified position, return that index

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

sol = Solution()

arr = [1, 3, 5, 6]
print(sol.searchInsert(arr, 5))
print(sol.searchInsert(arr, 2))
print(sol.searchInsert(arr, 7))
