class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        m=0
        for i in s:
            if i=='(':
                st.append(i)#count+=1
            elif i==')':
                st.pop()#count-=1
            if len(st)>m:#count>m
                m=len(st)#m=count
        return m
