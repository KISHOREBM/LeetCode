class Solution(object):
    def frequencySort(self, s):
        ret=""
        d=dict()
        for i in set(s):
            d[i]=s.count(i)
        s_values=[a for _,a in sorted(zip(list(d.values()),list(d.keys())))[::-1]]
        # print(sorted(zip(value,key)))
        for i in s_values:
            ret+=i*s.count(i)
        return ret


        


        