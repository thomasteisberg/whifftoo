from __future__ import division
import numpy as np
import math

import sys
sys.path.append("../simulation")
import simulator2d

class WhiffWorld():

    def __init__(self, dt):
        self.dt = dt
        self.state_dim_names = ['up_angle', 'up_angle_vel', 'up_angle_acc',
                                'servo', 'cgx', 'cgy', 'mix', 'miy']
        self.possible_actions = ['move -0.01', 'move 0', 'move 0.01']
        self.state = self.s0()

    def reinitialize(self):
        self.state = self.s0()

    def s0(self):
        initial_state = np.array([0 for i in range(len(self.state_dim_names))])
        return initial_state

    def step(self, state, action):
        # returns next state given the action
        action_map = {0: -0.01, 1: 0, 2: 0.01}
        state[3] += action_map[action.index(1)]

        state_dictionary = {}

        for state_name, state_element in zip(self.state_dim_names, state):
            state_dictionary[state_name] = state_element
        next_state_dictionary = simulator2d.simulate_timestep(state_dictionary, self.dt)

        next_state = []
        for name in self.state_dim_names:
            next_state.append(next_state_dictionary[name])
        return next_state

    def is_terminal(self, state):
        # state is terminal when copter is tilted more than 60 degrees
        shaft_angle = state[0]
        if abs(shaft_angle) > ():
            return True
        return False
