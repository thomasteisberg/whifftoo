import numpy as np

class LinearApproximation():

    def __init__(self):
        pass

    def get_features(self, state, action):
        # temporary: just appends state and action vectors (with a bias term)
        bias = np.array([1])
        return bias+state+action

    def get_Q_value(self, state, action, weights):
        # returns Q value of (state,action) by taking dot 
        # product with weight vector
        sa = self.get_features(state, action)
        return np.dot(sa, weights)

    def bestAction(self, state, possible_actions, weights):
        # returns index of action with largest Q value
        Q_values = [self.get_Q_value(state, action, weights) for action in possible_actions]
        return Q_values.index(max(Q_values))

