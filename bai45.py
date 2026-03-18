class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        n=highLimit
        nn=lowLimit
        kk=[0]*(n+1)
        for i in range(nn,n+1):
            if i<10:
                kk[i]=1
            else:
                j=str(i)
                summ=0
                for i in j:
                    summ+=int(i)
                if kk[summ]>0:
                    kk[summ]+=1
                else:
                    kk[summ]=1
        return max(kk)
        