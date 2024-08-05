package FirstLastPos;

class Solution {
    public int[] searchHelper(int[] nums, int left, int right, int target) {
        // Base Case 1 – bounds have crossed over, so target is not present
        if (left > right) {
            int[] result = {-1, -1};
            return result;
        }

        // Base Case 2 – only one element in range.
        if (left == right) {
            //Check that it matches the target – if so, return index
            if (nums[left] == target) {
                int[] result = {left, right};
                return result;
            //Otherwise, value not present in range
            } else {
                int[] result = {-1, -1};
                return result;
            }
        }

        int mid = (left+right)/2; // Compute midpoint

        //Isolate region to recurse over, if midpoint does not match target
        if (nums[mid] > target) {
            return searchHelper(nums, left, mid-1, target);
        } else if (nums[mid] < target) {
            return searchHelper(nums, mid+1, right, target);
        }

        //Compute the bounds to the left and right of the midpoint
        int[] leftbounds = searchHelper(nums, left, mid, target);
        int[] rightbounds = searchHelper(nums, mid+1, right, target);

        //If the value is not found in either portion, just return the other range
        if (leftbounds[0] == -1) {
            return rightbounds;
        } else if (rightbounds[1] == -1) {
            return leftbounds;
        }
        
        //Consolidate indices
        int[] result = {leftbounds[0], rightbounds[1]};
        return result;
    }

    public int[] searchRange(int[] nums, int target) {
        return searchHelper(nums, 0, nums.length-1, target);
    }
}