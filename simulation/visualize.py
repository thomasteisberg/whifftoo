import pygame
import sys
import math

from constants import *
import simulator2d as sim

# Colors!
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

ORIGIN = (500, 150)
s = {'up_angle': 0, 
     'up_angle_vel' : 0,
     'up_angle_acc' : 0,
     'servo': math.pi/3, 
     'cgx': 0,
     'cgy': 0,
     'mi': 0
     }   

# scale lengths
scale_arm_length = 300 * (arm_length/(arm_length + mass_length_cg))
scale_mass_length = 300 * (mass_length_cg/(arm_length + mass_length_cg))
pixels_per_length = 300 / (mass_length_cg + arm_length)

# Pygame init
pygame.init()
screen = pygame.display.set_mode((1000,500))

def toscreen(pt):
    return (pt[0] + ORIGIN[0], pt[1] + ORIGIN[1])

def arm_endpoint(s):
    actual_angle = ((3*math.pi)/2) - s['up_angle'] 
    return (scale_arm_length * math.cos(actual_angle), -scale_arm_length * math.sin(actual_angle))

def rotating_mass_endpoint(s):
    servo_pos = arm_endpoint(s)
    actual_angle = ((3*math.pi)/2) - s['up_angle'] 
    return (servo_pos[0] - (-scale_mass_length * math.cos(actual_angle-s['servo'])), \
            servo_pos[1] - (scale_mass_length * math.sin(actual_angle-s['servo']))) 

def scale_pt(pt, increment=0):
    return (pt[0] * pixels_per_length + increment, pt[1] * pixels_per_length + increment)

def display_configuration(state):
    
    screen.fill(black)

    servo_end = rotating_mass_endpoint(state)
    arm_end = arm_endpoint(state)

    points = [toscreen((0, 0)), toscreen(arm_end)]
    pygame.draw.lines(screen, red, False, points, 2)
    points = [toscreen(arm_end), toscreen(servo_end)]
    pygame.draw.lines(screen, green, False, points, 2)

    mg_pt = (state['cgx'], -state['cgy'])

    points = [toscreen(scale_pt(mg_pt)), toscreen(scale_pt(mg_pt, 3))]
    pygame.draw.lines(screen, white, False, points, 10)
    pygame.display.update()


direction = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();

    display_configuration(s)
    pygame.time.delay(10)
    s = sim.simulate_timestep(s, 0.1)

