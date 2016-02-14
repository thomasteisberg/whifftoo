from __future__ import division
import numpy as np
import math
import random

import sys
sys.path.append("../simulation")
import simulator2d

class WhiffWorld():

    def __init__(self, dt):
        self.dt = dt
        self.state_dim_names = ['up_angle', 'up_angle_vel', 'up_angle_acc',
                                'servo', 'cgx', 'cgy', 'mi']
        self.possible_actions = ['move -0.01', 'move 0', 'move 0.01']
        self.state = self.s0()

    def reinitialize(self):
        self.state = self.s0()

    def s0(self):
        initial_state = np.array([random.uniform(-math.pi/6, math.pi/6), \
                                  random.uniform(-0.08, 0.08), \
                                  random.uniform(-0.02, 0.02), \
                                  random.uniform(-math.pi/2, math.pi/2), \
                                  0, 0,  0])
        return initial_state

    def step(self, state, action):
        # print action
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

        self.state = next_state
        return next_state

    def is_terminal(self, state):
        # state is terminal when copter is tilted more than 60 degrees
        shaft_angle = state[0]
        servo_angle = state[3]

        if abs(servo_angle) > 1.56: return True
        # print shaft_angle
        if abs(shaft_angle) > 0.78:
            return True
        return False
