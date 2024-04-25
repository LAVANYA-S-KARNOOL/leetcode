class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=""
        i=head
        while i:
            s=s+str(i.val)
            i=i.next
        return int(s,2)
