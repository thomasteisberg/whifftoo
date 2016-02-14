# Constants.py, yo

dt             = 0.001    # seconds
mass_rotatable = 60      # grams - mass of each rotating mass
mass_rotor     = 30       # grams - mass of the rotor assembly
mass_servo     = 20       # grams - mass of the servo assembly
mass_arm       = 1        # grams  - Total mass of main arm including servos
mass           = mass_rotor + mass_servo + mass_rotatable + mass_arm # grams - total mass

# Moment of Inertia constants 
arm_length      = .05   # meters - Total length of the arm from the rotor to
                        #          the pivot point
arm_cg          = .03   # meters - Distance along the arm from the rotor to
                        #          the CG
mass_length_cg  = .02   # meters - The length from the servo to the CG of the
                        #          rotating mass
arm_mass = mass - mass_rotatable # grams  - Total mass of main arm including servos
