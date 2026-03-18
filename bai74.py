class Solution(object):
    def pickGifts(self, gifts, k):
        h=[-1*i for i in gifts]


        # importing "heapq" to implement heap queue
        import heapq
        import math

        heapq.heapify(h)
        for i in range(k):
            cur=heapq.heappop(h);
            heapq.heappush(h,-1*int(math.sqrt(-cur)))
        return -1*sum(h)