class Solution(object):
    def lemonadeChange(self, bills):
        d={5:0,10:0}
        t=0
        c=0
        for i in range(len(bills)):
            if (bills[i]==10 or bills[i]==20)  and d[5]==0:
                return False
            if bills[i]==5:
                c+=1
                d[5]=c
            if bills[i]==10 and d[5]!=0:
                c-=1
                t+=1
                d[10]=t
                d[5]=c
                continue
            if bills[i]==20 and (d[5]>=1 and d[10]>=1):
                c-=1
                t-=1
                d[5]=c
                d[10]=t
                continue
            if bills[i]==20 and (d[5]>=3):
                c-=3
                d[5]=c
                continue
            if bills[i]==20 and (d[5]<=2 and d[10]==0):
                return False
        return True
            

            

            
        
        