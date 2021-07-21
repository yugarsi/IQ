class LLNode:
  def __init__(self, val=None):
    self.val = val
    self.next = None
    
class Queue:
	def __init__(self):
  	
    self.start = None
    self.end = None

	def enque(self, val):
  	node = LLNode(val)
  	if self.end == None:
    	self.end = node
      self.start = node
  	else:
  		self.end.next = node
    	self.end = node
  	
  
  def deque(Self):
  	if self.start == None:
    	return False
    temp = self.start
    self.start = self.start.next
    if self.start is None:
    	self.end = None
    return temp
    