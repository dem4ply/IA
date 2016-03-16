import numpy as np

np.random.seed(1)

class Perseptron( object ):

	def __init__( self, number_of_inputs, threshold=1, weights=None ):
		self.number_of_inputs = number_of_inputs
		self.threshold = threshold
		if weights:
			weigths = np.random.random( ( number_of_inputs, ) )
		self.weigths = weigths
		self._l_weigths = len( weigths )

	def _sigma_function( self, inputs ):
		return reduce( lambda sum, ( i, w ): ( sum + i * w ),\
			zip( inputs, self.weigths ) )

	def stimulus( self, i, position ):
		
		if i < self._l_weigths:
			self.add_stack( ( i, position ) )
			if self._is_all_inputs_received():
				sigma = self._sigma_function()
				self._send_output( sigma )
		else:
			raise ValueError( "la posicion es mayor a la cantidad entradas" )

	def _add_stack( self, position )
