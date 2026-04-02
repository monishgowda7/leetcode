class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        for num in nums:
            if num in a:
                a[num]+=1

            else:
                a[num]=1 
                
        high=max(a,key=a.get)
        return high
