class Solution(object):
    def smallestEqual(self, nums):
        for u in range(len(nums)):
            if u % 10 == nums[u]:
                return u
        return -1
