class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Step 1: Sort the array
        nums.sort()
        # Step 2: Initialize the closest sum with a very large number
        closest_sum = float('inf')
        
        # Step 3: Iterate through the sorted array
        for i in range(len(nums) - 2):
            # Use two-pointer technique for the remaining part of the array
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if this sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Exact match found, return the sum
                    return target
        
        return closest_sum