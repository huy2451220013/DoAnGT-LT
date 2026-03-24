class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        slow = 0
        fast = 0
        while fast < leng:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        for i in range(slow,leng):
            nums[i] = 0
