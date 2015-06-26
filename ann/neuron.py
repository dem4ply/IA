from .synapse import Synapse
from .bypass import Bypass

class Neuron( object ):
	
	def __init__(self, bypass = None):
		self.synapses_in = []
		self.synapses_out = []
		if bypass:
			self.bypass = bypass
		else:
			self.bypass = Bypass()

		self.output = 0
