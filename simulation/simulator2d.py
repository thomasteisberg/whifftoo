from __future__ import division
import math

ex_state = {'up_angle': math.pi / 8,    # angle of the pendulum from vertical
            'up_angle_vel' : 0,         # angular velocity of the above
            'up_angle_acc' : 0,         # angular acceleration of the above
            'servo': math.pi / 16,    # servo angle 

dt = 0.001      # seconds
mass = 30       # grams     - total mass
mass_rotatable  # grams     - mass of each rotating mass


def simulate_timestep(s, dt, x_axis=True):
    # Calculate CG and moment of inertia
    cg = find_cg(s['up_angle'], s['servo']);
    mi = find_mi(s['up_angle'], s['servo']);
        
    
    # Calculate rotational acceleration and integrate for velocity and angle
    torque = mass * cg[1]
    rot_acc = torque * mi
    rot_vel = (rot_acc * dt) + s['up_angle_vel']
    rot     = (rot_vel * dt) + s['up_angle']
    
    # update state dictionary
    s['up_angle'] = rot
    s['up_angle_vel'] = rot_vel
    s['up_angle_acc'] = rot_acc
    s['cg'] = cg
    s['mi'] = mi

    return s

def find_cg(angle, servo_angle):
    return (0,0) # TODO: This is not correct

def find_mi(angle, servo_angle):
    return (0,0) # TODO: This is not correct

