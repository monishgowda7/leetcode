# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=[]

        while head:
            d.append(head.val) 
            head=head.next


        c=set(d)
        f=list(c)
        f.sort()  

        dummy=ListNode()
        temp=dummy

        for i in f:
            temp.next=ListNode(i)
            temp=temp.next

        return dummy.next    
