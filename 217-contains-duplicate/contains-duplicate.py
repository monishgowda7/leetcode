class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}

        for n in nums:
            if n in d:
                d[n]+=1

            else:
                d[n]=1


        for i in d:
            if d[i] > 1:
                return True

            
        return False    

