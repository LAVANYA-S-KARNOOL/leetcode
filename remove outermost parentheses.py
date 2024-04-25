def removeOuterParentheses(self, s: str) -> str:
  count=0
        string=""
        for i in s:
            if i=='(':
                if count!=0:
                    string+=i
                count+=1
            else:
                if count!=1:
                    string+=i
                count-=1
        return string
