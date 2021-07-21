class Solution:
    def addNumString(self, num1, num2, carry):
        a = int(num1)
        b = int(num2)
        s = (a + b + carry)%10
        c = (a + b + carry)//10
        return [s,c]

    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        
        res = []
        c = 0
        while i>=0 or j>=0:
            if i>=0 and j>=0:
                [s,c] = self.addNumString(num1[i],num2[j],c)
            elif i<0:
                [s,c] = self.addNumString("0",num2[j],c)
            
            elif j<0:
                [s,c] = self.addNumString(num1[i],"0",c)
            
            res.append(str(s))
            
            i-=1
            j-=1
        if c == 1:
            res.append("1")
        
        sumstr=""
        for i in range(len(res)-1, -1, -1):
            sumstr += res[i]
        
        return sumstr
        
        