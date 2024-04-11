class Solution(object):
    def merge(self, nums1, m, nums2, n):
        t1 = m-1 #Tracker 1
        t2 = n-1 #Tracker 2
        next_open_index = len(nums1) - 1 #Next open insertion index

        while t1 >= 0 and t2 >= 0: #Iterate while both lists have elements
            if nums1[t1] > nums2[t2]:
                nums1[next_open_index] = nums1[t1] #Update new location
                nums1[t1] = 0 #Set original location to empty
                t1 -= 1
            else:
                nums1[next_open_index] = nums2[t2] #Update new location
                t2 -= 1
            next_open_index -= 1
        
        while t1 >= 0: #Leftover elements of t1
            nums1[next_open_index] = nums1[t1]
            t1 -= 1
            next_open_index -= 1
        
        while t2 >= 0: #Leftover elemnts of t2
            nums1[next_open_index] = nums2[t2]
            t2 -= 1
            next_open_index -= 1


sol = Solution()
arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 6]
sol.merge(arr1, len(arr1), arr2, len(arr2))
print(arr1)