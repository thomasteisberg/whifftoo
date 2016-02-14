from __future__ import division
import math

ex_state = {'up_angle': math.pi / 8,    # angle of the pendulum from vertical
            'up_angle_vel' : 0,         # angular velocity of the above
            'up_angle_acc' : 0,         # angular acceleration of the above
            'servo': math.pi / 16       # servo angle 
            'rotor_pos': (0,0)          # rotor position in plane (ground ref.)
           }

dt             = 0.001    # seconds
mass_rotatable = 2        # grams - mass of each rotating mass
mass_rotor     = 30       # grams - mass of the rotor assembly
mass_servo     = 20       # grams - mass of the servo assembly
shaft_length   = 10       # cm    - length of shaft from rotor to servo box
mass           = mass_rotor + mass_servo + mass_rotatable # grams - total mass


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

    mass_list = []
    mass_list.append(increment([0, 0], mass_rotor, \
            [0, 0]))
    servo_pos = [shaft_length * cos(angle), shaft_length * sin(angle)]
    mass_list.append(increment([0, 0], mass_servo, servo_pos))
    mass_list.append(increment([0, 0], mass_rotatable, \
            [, ]))
 
    return increment([0, 0], 1/mass, \
                    reduce(lambda x,y: [x[0]+y[0], y[1]+y[1]], mass_list)) 

def find_mi(angle, servo_angle):
    return (0,0) # TODO: This is not correct

#thx 221
def dotProduct(d1, d2):
    if len(d1) < len(d2):
        return dotProduct(d2, d1) 
    else:
        return sum(d1.get(f, 0) * v for f, v in d2.items())

def increment(d1, scale, d2):
    for f, v in d2.items():
        d1[f] = d1.get(f, 0) + v * scale
