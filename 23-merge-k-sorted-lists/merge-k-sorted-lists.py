# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        li=[]
        for i in lists:
            j=i
            while j!=None:
                li.append(j.val)
                j=j.next
        if len(li)==0:
            return 
        li.sort()

        head=ListNode()
        cur=head
        for i in range(len(li)):
            if i==0:
                head.val=li[i]
                head.next=None
            else:
                temp=ListNode(li[i],None)
                cur.next=temp
                cur=cur.next
        return head

        