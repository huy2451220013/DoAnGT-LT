class Solution(object):
    def sortEvenOdd(self, nums):
        odd = []
        even = []
        final = []
		
		#split
        for i in range(len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
		#sort
        even = sorted(even)
        odd = sorted(odd,reverse = True)
        pos = 0
		
		#combine
        while(True):
            if pos<len(even):
                final.append(even[pos])
            if pos<len(odd):
                final.append(odd[pos])
            pos+=1
            if pos == max(len(even),len(odd)):
                break
				
        return final
                
            