class Solution:
    def defangIPaddr(self, address: str) -> str:
        c=address.replace('.','[.]')
        return c   
