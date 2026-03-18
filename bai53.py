class Solution(object):
    def maxDistance(self, colors):
        max_dist=0
        for left in range(len(colors)-1):
            
            for right in range(left,len(colors)):
                if colors[left] != colors[right]:
                    curr_dist=right-left
                    max_dist=max(curr_dist,max_dist)
                    
                else:
                    continue
           
        return max_dist
        