class Synapse( object ):

	def __init__( self, neuron = None, weigth = 0 ):
		self.weigth = weigth
		self.neuron = neuron

	def __str__( self ):
		return "Weigth: {0}".format( self.weigth )

	def __repr__( self ):
		return "W: {0}".format( self.weigth )
