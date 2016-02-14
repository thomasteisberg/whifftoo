from __future__ import division
import math
from constants import *

ex_state = {'up_angle': math.pi / 8,    # angle of the pendulum from vertical
            'up_angle_vel' : 0,         # angular velocity of the above
            'up_angle_acc' : 0,         # angular acceleration of the above
            'servo': math.pi / 16,      # servo angle 
            'cgx': 0,
            'cgy': 0,
            'mi': 0
           }

def simulate_timestep(s, dt):
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
    s['cgx'] = cg[0]
    s['cgy'] = cg[1]
    s['mi'] = mi

    return s

def find_cg(angle, servo_angle):

    angle_from_rotor = ((3*math.pi)/2) - angle 
    servo_pos = [arm_length * math.cos(angle_from_rotor), arm_length * math.sin(angle_from_rotor)]

    mass_list = []
    # point 0 - mass at rotor
    mass_list.append(scalar([0, 0], mass_rotor))
    # point 1 - mass in arm
    mass_list.append(scalar(scalar(servo_pos, 0.5), mass_arm))
    # point 2 - mass in servo block 
    mass_list.append(scalar(servo_pos, mass_servo))
    # point 3 - mass in rotational block
    mass_list.append(scalar(
            [servo_pos[0] - (mass_length_cg * math.cos(angle - servo_angle)), \
             servo_pos[1] - (mass_length_cg * math.sin(angle - servo_angle))], \
            mass_rotatable))

    return scalar(reduce(lambda x,y: [x[0]+y[0], x[1]+y[1]], mass_list), 1/mass) 

def find_mi(angle, servo_angle):
    # point 1 - main arm
    points = []
    ints = []
    # point 1 - main arm
    x = arm_cg * math.sin(angle)
    y = arm_cg * math.cos(angle)
    points += [(x,y,arm_mass)]
    # point 2 - rotatable mass
    x = x - (mass_length_cg * math.cos(angle + servo_angle))
    y = y + (mass_length_cg * math.sin(angle + servo_angle))
    points += [(x,y,rotatable_mass)]
    return mi_point_masses(points)


# Moment of Inertia Helper Functions
def mi_point_masses(points):
    mi = 0.0
    for pt in points:
        # calculate the radius squared
        r = pt[0]*pt[0] + pt[1]*pt[1]
        mi += r * pt[2] # moment of inertia contribution = m*r^2
    return mi

#thx 221
def dotProduct(d1, d2):
    if len(d1) < len(d2):
        return dotProduct(d2, d1) 
    else:
        return sum(d1.get(f, 0) * v for f, v in d2.items())

def scalar(d1, scale):
    d2 = []
    for v in d1:
        d2.append(v * scale)
    return d2
