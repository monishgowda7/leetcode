class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= s.strip()
        s=s.lower()
        clean=""
        for ch in s:
            if ch.isalnum():

                clean=clean+ch


        rev=""
        for i in clean:
            rev=i+rev


        if clean==rev:
            return True

        else:
            return False        