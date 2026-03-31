class Solution(object):
    def checkIfExist(self, arr):
        l=len(arr)
        r=False
        for i in range(l):
            for j in range(l):
                if arr[i]==2*arr[j] and i!=j:
                    r=True
                    break
        return r
        


        
