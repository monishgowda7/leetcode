class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # for i in nums1[m:]:
            
        #     if i==0:
        #         nums1.remove(i)


        # for j in nums2[:n+1]:
        #     if j==0:
        #         nums2.remove(j)        


        # nums1.sort()
        # nums2.sort()

        # nums1.extend(nums2)
        
        # nums1.sort()
        
        del nums1[m:]
        nums1.extend(nums2[:n])
        nums1.sort()