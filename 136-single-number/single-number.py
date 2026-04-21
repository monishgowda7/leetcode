class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for n in nums:
            if n in d:
                d[n]+=1

            else:
                d[n]=1



        for i in d:
            if d[i]==1:
                return i
