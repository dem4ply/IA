class Bypass( object ):
	
	def __init__( self, bypass = 0, weigth = 0 ):
		self.bypass = bypass
		self.weigth = weigth

	def __str__( self ):
		return "Bypass: {0}, Weigth: {1}, Eval: {2}".format(
			self.bypass, self.weigth, self.eval() )

	def __repr__( self ):
		return "B: {0}, W: {1}, E: {2}".format(
			self.bypass, self.weigth, self.eval() )

	def eval( self ):
		return self.bypass * self.weigth
