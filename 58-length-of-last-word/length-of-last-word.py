class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
        r=s.strip()
        v=r.split(" ")
        
        p=len(v)
        m=[]
        for i in range(p):
            # for j in v:
            if i==p-1:
               
                for j in v[p-1]:
                    m.append(j)
 
                return len(m)    





                # for j in v:
                #     for char in j:
                #         m.append(char)

                #     return len(m)            
 


            # if i==len(v):
            #     for char in i:
            #         m.append(i)

            # return len(m)


