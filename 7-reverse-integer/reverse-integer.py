class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg=x<0

        if x<0:
            x=abs(x)

        a=[]
        for i in str(x):
            a.append(i)
        

        c=a[::-1]
        # print(c)  
        d="".join(c)
        l=int(d)


        if l>=2**31 - 1 or l<=-2**31:
            return 0



        if neg:
            return -1*l

        else:
            return l    
