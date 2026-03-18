class Solution:
    def timeRequiredToBuy(self, tickets, k):
        dummy = tickets[:]
        n = len(dummy)
        timer = 0
        i = 0

        while dummy[k] != 0:
            if dummy[i % n] != 0:
                dummy[i % n] -= 1
                timer += 1
            i += 1

        return timer
