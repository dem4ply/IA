from ann.bypass import Bypass
import unittest

class Test_bypass(unittest.TestCase):
	
	def test_string_output_default( self ):
		bypass = Bypass()
		self.assertEqual( str( bypass ), "Bypass: 0, Weigth: 0, Eval: 0" )
		self.assertEqual( repr( bypass ), "B: 0, W: 0, E: 0" )

	def test_string_output_with_params( self ):
		bypass = Bypass( bypass = 10, weigth = 12 )
		self.assertEqual( str( bypass ), "Bypass: 10, Weigth: 12, Eval: 120" )
		self.assertEqual( repr( bypass ), "B: 10, W: 12, E: 120" )

	def test_eval( self ):
		bypass = Bypass()
		self.assertEqual( bypass.eval(), 0 )
		bypass = Bypass( bypass = 10, weigth = 12 )
		self.assertEqual( bypass.eval(), 120 )


if __name__ == '__main__':
    unittest.main()
