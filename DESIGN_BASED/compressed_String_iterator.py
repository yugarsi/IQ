class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.pre = compressedString[0]
        self.repeat = 0
        self.curIndex = 0
    
    def next(self) -> str:
        if not self.hasNext():
            return " "
    
        self.repeat -= 1
        return self.pre
      

    def hasNext(self) -> bool:
        # There is still remainings.
        if self.repeat > 0:
            return True
    
        # Breakdown into alpha + number block (e.g. L12)
        if self.curIndex < len(self.compressedString) and            self.compressedString[self.curIndex].isalpha():
            # Process alpha part.
            self.pre = self.compressedString[self.curIndex]
            self.curIndex += 1
            self.repeat = 0

            rep = ""
            while self.curIndex < len(self.compressedString) and \
                self.compressedString[self.curIndex].isdigit():
                rep += self.compressedString[self.curIndex]
                self.curIndex += 1
            self.repeat = int(rep)
            return True
        
        return False