class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_map = {}

        for i, num in enumerate(nums):
            if num in num_map and i - num_map[num] <= k:
                return True
            num_map[num] = i

        return False
