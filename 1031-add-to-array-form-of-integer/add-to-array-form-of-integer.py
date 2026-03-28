class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        # n=sum(num)
        m=map(str,num)
        string="".join(m)
        s=int(string)
        add=str(s+k)
        # lists=add.split(",")
        # i=list(map(int,lists))
        i=[]
        for k in add:
            i.append(int(k))

        return i









        