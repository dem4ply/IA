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

	def test_is_synapse_in( self )

if __name__ == '__main__':
    unittest.main()
