from ann.synapse import Synapse
import unittest

class Test_synapse(unittest.TestCase):
	
	def test_string_output_default( self ):
		synapse = Synapse()
		self.assertEqual( str( synapse ), "Weigth: 0" )
		self.assertEqual( repr( synapse ), "W: 0" )

	def test_string_output_with_params( self ):
		synapse = Synapse( weigth = 12 )
		self.assertEqual( str( synapse ), "Weigth: 12" )
		self.assertEqual( repr( synapse ), "W: 12" )

	def test_eval( self ):
		synapse = Synapse( neuron = 10, weigth = 4 )
		self.assertEqual( synapse.eval(), 40 )

	def test_is_synapse_in( self ):
		synapse = Synapse( neuron = 10, weigth = 4 )
		self.assertEqual( synapse.is_in(), True )
		self.assertEqual( synapse.eval(), 40 )
