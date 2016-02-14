import numpy as np

class WhiffWorld():

	def __init__(self):
		self.state = self.s0()
		self.state_dim_names = ['shaft_angle', 'servo_angle']
		self.possible_actions = ['move 0',
								 'move 0.01', 'move 0.02', 'move 0.03', 
								 'move -0.01, move -0.02', 'move -0.03']

	def reinitialize(self):
		self.state = self.s0()

	def s0(self):
		initial_state = np.array([0,0.1])
		return initial_state

	def step(self, state, action):
		# returns next state and reward
		# TODO: INTEGRATE SIMULATOR HERE

	def is_terminal(self, state):
		# state is terminal when copter is tilted more than 60 degrees
		shaft_angle = state[0]
		sixty_degree_approx = 1.05  # in radians
		if abs(shaft_angle) > sixty_degree_approx:
			return True
		return False
