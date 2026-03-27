class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # m="".join(nums)
        s=set()
        for i in nums:
            s.add(i)


        a=list(s)
        a.sort()
        
        for j in range(0,len(a)):
            nums[j]=a[j]


        return len(a)    
        





        # s=nums.remove.duplicate
        # return len(s)

        
        