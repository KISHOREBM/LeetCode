class Solution(object):
    def lemonadeChange(self, bills):
        coins={
            5:0,10:0,20:0
        }
        values=[20,10,5]
        for i in bills:
            if i!=5:
                amount=i-5
                j=0
                while j<len(values) and   amount>0:
                    x=(amount//values[j])
                    if coins[values[j]]-x>=0:
                        coins[values[j]]-=x
                        amount=amount%values[j]
                    j+=1
                if amount>0:
                    return False
            coins[i]+=1
            # print(coins,'co')
        return True
            

        