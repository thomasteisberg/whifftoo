import pygame
import sys
import math

from constants import *

# Colors!
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

ORIGIN = (500, 50)
s = {'up_angle': math.pi/2, 
     'up_angle_vel' : 0,
     'up_angle_acc' : 0,
     'servo': math.pi/2, 
     'cg': [0,0],
     'mi': [0,0]
     }   

# scale lengths
scale_arm_length = 300 * (arm_length/(arm_length + mass_length_cg))
scale_mass_length = 300 * (mass_length_cg/(arm_length + mass_length_cg))

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

def display_configuration(state):
    
    screen.fill(black)

    servo_end = rotating_mass_endpoint(state)
    arm_end = arm_endpoint(state)

    points = [toscreen((0, 0)), toscreen(arm_end)]
    pygame.draw.lines(screen, red, False, points, 2)
    points = [toscreen(arm_end), toscreen(servo_end)]
    pygame.draw.lines(screen, green, False, points, 2)
    pygame.display.update()

# test!
screen.fill(black)

while s['up_angle'] >= -math.pi/2:
    while s['servo'] >= -math.pi/2:
        display_configuration(s)
        s['servo'] -= math.pi/16
    s['servo'] = math.pi/2
    s['up_angle'] -= math.pi/128

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
