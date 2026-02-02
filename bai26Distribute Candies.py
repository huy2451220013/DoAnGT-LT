class Solution(object):
    def distributeCandies(self, candyType):
        seen=set()
        n=len(candyType)
        count=0
        i=0
        while count<n/2 and i<n:
            if candyType[i] not in seen:
                seen.add(candyType[i])
                count+=1
                i+=1
            else:
                i+=1
        return count
