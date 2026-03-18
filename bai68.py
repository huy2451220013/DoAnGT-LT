class Solution(object):
    def prefixCount(self, words, pref):
        l=len(pref)
        c=0
        for i in words:
            if i[:l]==pref:
                c+=1
        return c
        