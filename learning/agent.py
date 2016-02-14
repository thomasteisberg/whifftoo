import numpy as np
import sys
sys.path.append("../simulation")
import visualize

class QLearner():

  def __init__(self, policy, representation, discount_rate = 0.8, learning_rate = 0.01, seed = 2):
    self.representation = representation
    self.policy = policy
    self.discount_rate = discount_rate
    self.learning_rate = learning_rate
    self.random_state = np.random.RandomState()
    weight_dimension = 11
    self.weights = np.array([self.random_state.rand()-0.5 for i in range(weight_dimension)], dtype = float)
    print self.weights
  
  def future_action(self, state, possible_actions):
    # Q learner chooses optimal action
    return self.policy.get_best_action(state, possible_actions, self.weights)
  
  def learn(self, state, action, reward, next_state, possible_actions):

    disp_state = {'up_angle': state[0], 'up_angle_vel': state[1], 'up_angle_acc': state[2], 'servo': state[3], 'cgx': state[4], 'cgy': state[5], 'mi': state[6]}
    visualize.display_configuration(disp_state); 

    # w <-- w + learning_rate * (reward + discount_rate * max[Q(s', a')] - Q(s,a)) * (gradient of Q(s,a) wrt weights)
    # gradient of Q(s,a) wrt weights is (state, action) pair representation
    max_Q_s_prime_a_prime = self.representation.get_Q_value(next_state, self.future_action(state, possible_actions), self.weights)
    Q_s_a = self.representation.get_Q_value(state, action, self.weights)
    state_action_feature_vector = self.representation.get_features(state, action)
    new_weights = self.weights + (self.learning_rate * (reward + self.discount_rate * max_Q_s_prime_a_prime - Q_s_a)) * state_action_feature_vector
    self.weights = new_weights
