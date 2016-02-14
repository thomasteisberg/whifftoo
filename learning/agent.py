import numpy as np

class QLearner():

  def __init__(self, policy, representation, discount_rate = 0.8, learning_rate = 0.05, seed = 1):
    self.representation = representation
    self.policy = policy
    self.discount_rate = discount_rate
    self.learning_rate = learning_rate
    self.random_state = np.random.RandomState(seed=seed)
    weight_dimension = 12
    self.weights = np.array([self.random_state.rand()-0.5 for i in range(weight_dimension)], dtype = float)
  
  def future_action(self, state, possible_actions):
    # Q learner chooses optimal action
    return self.policy.get_best_action(state, possible_actions)
  
  def learn(state, action, reward, next_state, possible_actions, is_terminal):
    # w <-- w + learning_rate * (reward + discount_rate * max[Q(s', a')] - Q(s,a)) * (gradient of Q(s,a) wrt weights)
    # gradient of Q(s,a) wrt weights is (state, action) pair representation
    max_Q_s_prime_a_prime = representation.get_Q_value(next_state, self.future_action(state, possible_actions), weights)
    Q_s_a = representation.get_Q_value(state, action, weights)
    state_action_feature_vector = representation.get_features(state, action)
    new_weights = self.weights + (learning_rate * (reward + discount_rate * max_Q_prime_a_prime - Q_s_a)) * state_action_feature_vector
    self.weights = new_weights
