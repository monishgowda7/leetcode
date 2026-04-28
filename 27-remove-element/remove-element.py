class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # for i in nums:
        #     if i==val:
        #         nums.remove(i)
        #         # nums.append(_)    

        # for i in nums:
        #     if i==val:
        #         nums.remove(i)
        
        
        # for i in nums:
        #     if i==val:
        #         nums.remove(i)

        # return len(nums)        
        k=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
                

        return k       