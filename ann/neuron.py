from synapse import Synapse

class Neuron( object ):
	
	def __init__(self):
		self.synapses_in = []
		self.synapses_out = []
