from __future__ import division
import math

ex_state = {'up_angle': math.pi / 8,    # angle of the pendulum from vertical
            'up_angle_vel' : 0,         # angular velocity of the above
            'up_angle_acc' : 0,         # angular acceleration of the above
            'servo_x': math.pi / 16,    # x servo angle 
            'servo_y': math.pi / 16}    # y servo angle

dt = 0.001

def simulate_timestep(in_state, dt):
    #cg = find_cg(in_state['servo_a'], in_state['servo_b']);
    #torque = calc_torque()
    # more stuff
    return in_state

