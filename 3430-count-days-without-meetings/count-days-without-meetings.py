class Solution(object):
    def countDays(self, days, meetings):
        meetings.sort()
        
        count=meetings[0][0]-1
        # print(count)
        start=meetings[0][1]
        for i in meetings[1:]:
            if start>=i[0]:
                start=max(start,i[1])
            else:
                count+=i[0]-start-1
                start=max(start,i[1])
            # print(start)
        count+=days-start
        return count



        