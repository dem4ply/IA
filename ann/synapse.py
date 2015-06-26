class Synapse( object ):

	def __init__( self, neuron = None, weigth = 0 ):
		self.weigth = weigth
		if ( isinstance( neuron, ( int, float ) ) ):
			self._is_in = True
		else:
			self._is_in = False
		self.neuron = neuron

	def __str__( self ):
		return "Weigth: {0}".format( self.weigth )

	def __repr__( self ):
		return "W: {0}".format( self.weigth )

	def is_in( self ):
		return self._is_in

	def eval( self ):
		if self.is_in():
			return self.neuron * self.weigth
