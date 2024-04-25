class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        if i in s:
            if len(st)==0:
                st.append(i)
            elif st[-1]=='A' and i=='B':
                st.pop()
            elif st[-1]=='C' and i=='D':
                st.pop()
        
