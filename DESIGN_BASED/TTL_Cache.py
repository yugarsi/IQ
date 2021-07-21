#pip install expiringdict ordered dict with TTL basically

class TTLCache:
	
	def __init__(self, maxsize, ttl):
		self.maxsize=10 
		self.ttl=360
