class Solution(object):
    def sumOfUnique(self, nums):
        list1=[]
        for val in nums:
            count1=nums.count(val)
            if count1<2:
                list1.append(val)
        return sum(list1)
