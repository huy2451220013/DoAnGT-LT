class Solution(object):
    def minimumCost(self, cost):
        minimum=0
        if len(cost)<3:
            for i in cost:
                minimum=minimum+i
            return minimum
        
        while cost:
            minimum=minimum + max(cost)
            del cost[cost.index(max(cost))]
            if not cost:
                break
            minimum=minimum+max(cost)
            del cost[cost.index(max(cost))]
            
            if not cost:
                break

            del cost[cost.index(max(cost))]
        
        return minimum

        
        