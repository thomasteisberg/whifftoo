import numpy as np

class eGreedy():
	## chooses greedy action (i.e. action with maximum Q-value)
	## with probability (1-epsilon). Otherwise chooses uniformly
	## random action for exploration.
	def __init__(self, representation, epsilon = 0.1, seed = 1):
		self.epsilon = epsilon
		self.old_epsilon = epsilon
		self.representation = representation
		self.random_state = np.random.RandomState(seed=seed)

	def pi(self, state, possible_actions):
		random_draw = self.random_state.rand()
		# explore: pick random action
		if coin < self.epsilon:
			action_index = self.random_state.choice(possible_actions)
			action = [0 for i in possible_actions]
			action[action_index] += 1
			return action
		# else exploit: pick greedy action
		return self.get_best_action(state, possible_actions)

	def get_best_action(self, state, possible_actions):
		best_action_index = self.representation.bestAction(state, possible_actions)
		action = [0 for i in possible_actions]
		action[best_action_index] += 1
		return action

	def turn_on_exploration(self):
		self.epsilon = self.old_epsilon
		
	def turn_off_exploration(self):
		self.old_epsilon = self.epsilon
		self.epsilon = 0



