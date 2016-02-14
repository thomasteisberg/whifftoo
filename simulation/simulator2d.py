from __future__ import division
import math

ex_state = {'up_angle': math.pi / 8,    # angle of the pendulum from vertical
            'up_angle_vel' : 0,         # angular velocity of the above
            'up_angle_acc' : 0,         # angular acceleration of the above
            'servo': math.pi / 16,    # servo angle 

dt = 0.001      # seconds
mass = 30       # grams     - total mass
mass_rotatable  # grams     - mass of each rotating mass


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
    s['cg'] = cg
    s['mi'] = mi

    return s

def find_cg(angle, servo_angle):
    points = []
    # point 1 - main arm
    x = arm_cg * math.sin(angle)
    y = arm_cg * math.cos(angle)
    points += [(x,y,arm_mass)]
    # point 2 - rotatable mass
    x = x - (mass_length_cg * math.cos(angle + servo_angle))
    y = y + (mass_length_cg * math.sin(angle + servo_angle))
    points += [(x,y,rotatable_mass)]
    return mi_point_masses(points)

def find_mi(angle, servo_angle):
    return (0,0) # TODO: This is not correct

# Moment of Inertia Helper Functions

arm_length      = .05   # meters - Total length of the arm from the rotor to
                        #          the pivot point
arm_cg          = .03   # meters - Distance along the arm from the rotor to
                        #          the CG
arm_mass        = 20    # grams  - Total mass of main arm including servos
mass_length_cg  = .01   # meters - The length from the servo to the CG of the
                        #          rotating mass

def mi_point_masses(points):
    mi = 0.0
    for pt in points:
        # calculate the radius squared
        r = pt[0]*pt[0] + pt[1]*pt[1]
        mi += r * pt[2] # moment of inertia contribution = m*r^2
    return mi
