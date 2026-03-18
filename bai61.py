class Solution(object):
    def countElements(self, nums):
        if len(nums)==1 or nums.count(nums[0])==len(nums):
            return 0
        nums=sorted(nums)
        return len(nums)-nums.count(nums[0])-nums.count(nums[-1])
        