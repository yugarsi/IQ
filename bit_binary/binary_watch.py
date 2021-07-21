class Solution:
    def readBinaryWatch(self, turnedOn):
        res = []
        for hour in range(12):
            for minute in range(60):
                hbits = bin(hour)[2:].count('1')
                mbits = bin(minute)[2:].count('1')
                if hbits + mbits == turnedOn:
                    res.append(f"{hour}:{minute:02}")
            
        return res    

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
		result = []
		options = "h8 h4 h2 h1 m32 m16 m8 m4 m2 m1".split()
		for opt in combinations(options, turnedOn):
		hour = 0
		minute = 0
		for value in opt:
		  if value[0] == 'h':
		    hour += int(value[1:]) #find integer value of hour
		  else:
		    minute += int(value[1:]) #finds integer value of minute
		if hour > 11 or minute > 59:
		  continue
		result.append(f"{hour}:{minute:02}")
		return result

                    
        
        