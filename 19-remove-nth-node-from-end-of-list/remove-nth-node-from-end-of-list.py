# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head or not head.next:
            return None
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        cur=head
        for i in range(count-n-1):
            cur=cur.next
        # if count==2:
        #     if n==1:
        #         head.next=None
        #         return head
        #     return head.next
        if cur==head:
            if count==n:
                return head.next
        cur.next=cur.next.next
        return head
        