class Solution(object):
    def twoSum(self, numbers, target):
        r=[]
        for i in range(len(numbers)):
            t=target-numbers[i]
            l=i+1
            h=len(numbers)-1
            while l<=h:
                m=l+(h-l)//2
                if numbers[m]==t:
                    return [i+1,m+1]
                elif numbers[m]>t:
                    h=m-1
                else:
                    l=m+1
              
            
        