class Solution(object):
    def removeDuplicates(self, nums):
        discrete_count = 0

        for x in range(len(nums)-1):
            if nums[x] < nums[x+1]:
                nums[discrete_count] = nums[x]
                nums[discrete_count+1] = nums[x+1]
                discrete_count += 1
        
        return discrete_count
    
arr = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(arr))
print(arr)