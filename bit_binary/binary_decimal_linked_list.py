class Solution(object):
    def getDecimalValue1(self, head):
        ll = 0
        cur = head
        while(cur):
            ll += 1
            cur = cur.next
            
        dec = 0
        cur = head
        while(cur):
            dec += cur.val * pow(2,ll-1)
            ll -= 1
            cur = cur.next
        
        return dec
    
    def getDecimalValueN(self, head):
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num
    
    ###Left shift by 1 [ << 1 multiplies by two ]  (|) adds 
    def getDecimalValue(self, head):
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val #
            head = head.next
        return num