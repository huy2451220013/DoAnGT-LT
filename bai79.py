class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        ans=1
        for num in range(1,len(nums)):
            if nums[num]!=nums[num-1]:
                nums[ans]=nums[num]
                ans+=1
        return ans