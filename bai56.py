class Solution(object):
    def mostWordsFound(self, sentences):
        count=0
        for ch in sentences:
            word=len(ch.split())
            count=max(count,word)
        return count