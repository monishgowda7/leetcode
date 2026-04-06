# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        v=[]

        while list1:
            v.append(list1.val)
            list1=list1.next

        while list2:
            v.append(list2.val)
            list2=list2.next    


        v.sort()
        
        dummy=ListNode()
        temp=dummy

        for i in v:
            temp.next=ListNode(i)
            temp =temp.next


        return dummy.next     



