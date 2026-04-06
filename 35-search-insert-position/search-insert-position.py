class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        d={}

        for i, num in enumerate(nums):
            d[num]=i
            if int(num)==target:
                return d[num]

            elif num> target:
                return i


        return len(nums)              
                  

                