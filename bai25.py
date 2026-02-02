class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        count=0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1]-timeSeries[i]<duration:
                count+=timeSeries[i+1]-timeSeries[i]
            elif timeSeries[i+1]-timeSeries[i]>=duration:
                count+=duration
        count+=duration
        return count
                
            