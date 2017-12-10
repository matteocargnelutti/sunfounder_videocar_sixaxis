#!/usr/bin/env python
#
# sunfounder_videocar_sixaxis
# Python Script to control the Sunfounder Smart Video Car with a PS3 Controller.
#
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import RPi.GPIO as GPIO
import pygame
import video_dir
import car_dir
import motor
import sys
from time import ctime, sleep 

#-----------------------------------------------------------------------------
# Config & motors setup
#-----------------------------------------------------------------------------
busnum = 1 # Edit busnum to 0, if you uses Raspberry Pi 1 or 0

# Init motors
video_dir.setup(busnum=busnum)
car_dir.setup(busnum=busnum)
motor.setup(busnum=busnum) 

# Set motors states
video_dir.home_x_y()
car_dir.home()
motor.setSpeed(100)

#-----------------------------------------------------------------------------
# Pygame and joystick setup
#-----------------------------------------------------------------------------
pygame.init()

# If there are no joystick 
if not pygame.joystick.get_count():
    print "No SIXAXIS found."
    pygame.quit()
    sys.exit()
# If there is a joystick
else:
    print "SIXAXIS ready."
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    buttons = joystick.get_numbuttons()

#-----------------------------------------------------------------------------
# Input mapping
#-----------------------------------------------------------------------------
# Joystick map 
# "used" = has the button been used on the last loop cycle ?
joystick_map = {}

# Car movements
joystick_map['forward'] = {"key": 14, "used": False} # Cross
joystick_map['backward'] = {"key": 15, "used": False} # Square
joystick_map['left'] = {"key": 7, "used": False} # Left button
joystick_map['right'] = {"key": 5, "used": False} # Right button

# Camera's servo movements
joystick_map['camera_x+'] = {"key": 11, "used": False} # R1
joystick_map['camera_x-'] = {"key": 9, "used": False}  # R2
joystick_map['camera_y+'] = {"key": 10, "used": False} # L1
joystick_map['camera_y-'] = {"key": 8, "used": False} # L2
joystick_map['camera_reset'] = {"key": 0, "used": False} # Select = reset position

#-----------------------------------------------------------------------------
# Catch input loop (every 0.1s)
#-----------------------------------------------------------------------------
while True:

    # Exit Script = ESC
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # For each button :
    # If the button is pressed :
    # - do the more appropriate action, mark the button as used
    # If the button is not pressed : 
    # - if it was pressed on the previous cycle,  do the appropriate clean-up action 
    if buttons != 0:
        # Forward : pressed
        if joystick.get_button(joystick_map['forward']['key']):
            print "Forward"
            motor.forward()
            joystick_map['forward']['used'] = True
        # Forward : released
        else:
            if joystick_map['forward']['used']: # If used on previous turn
                motor.stop()
                joystick_map['forward']['used'] = False

        # Backward : pressed
        if joystick.get_button(joystick_map['backward']['key']):
            print "Backward"
            motor.backward()
            joystick_map['backward']['used'] = True
        # Backward : released
        else:
            if joystick_map['backward']['used']: # If used on previous turn
                motor.stop()
                joystick_map['backward']['used'] = False

        # Left : pressed
        if joystick.get_button(joystick_map['left']['key']):
            print "Left"
            car_dir.turn_left()
            joystick_map['left']['used'] = True
        # Left : released
        else:
            if joystick_map['left']['used']: # If used on previous turn
                car_dir.home()
                joystick_map['left']['used'] = False

        # Right : pressed
        if joystick.get_button(joystick_map['right']['key']):
            print "Right"
            car_dir.turn_right()
            joystick_map['right']['used'] = True
        # Right : released
        else:
            if joystick_map['right']['used']: # If used on previous turn
                car_dir.home()
                joystick_map['right']['used'] = False
            
        # Camera x+ : pressed
        if joystick.get_button(joystick_map['camera_x+']['key']):
            print "camera_x+"
            video_dir.move_increase_x()
            joystick_map['camera_x+']['used'] = True
        # Camera x+ : released
        else:
            if joystick_map['camera_x+']['used']: # If used on previous turn
                #video_dir.home_x_y()
                joystick_map['camera_x+']['used'] = False
            
        # Camera x- : pressed
        if joystick.get_button(joystick_map['camera_x-']['key']):
            print "camera_x-"
            video_dir.move_decrease_x()
            joystick_map['camera_x-']['used'] = True
        # Camera x- : released
        else:
            if joystick_map['camera_x-']['used']: # If used on previous turn
                #video_dir.home_x_y()
                joystick_map['camera_x-']['used'] = False

        # Camera y+ : pressed
        if joystick.get_button(joystick_map['camera_y+']['key']):
            print "camera_y+"
            video_dir.move_increase_y()
            joystick_map['camera_y+']['used'] = True
        # Camera x+ : released
        else:
            if joystick_map['camera_y+']['used']: # If used on previous turn
                #video_dir.home_x_y()
                joystick_map['camera_y+']['used'] = False
            
        # Camera x- : pressed
        if joystick.get_button(joystick_map['camera_y-']['key']):
            print "camera_y-"
            video_dir.move_decrease_y()
            joystick_map['camera_y-']['used'] = True
        # Camera x- : released
        else:
            if joystick_map['camera_y-']['used']: # If used on previous turn
                #video_dir.home_x_y()
                joystick_map['camera_y-']['used'] = False
        
        # Camera reset : pressed
        if joystick.get_button(joystick_map['camera_reset']['key']):
            print "camera_reset"
            video_dir.home_x_y()
            joystick_map['camera_reset']['used'] = True
        # Camera x- : released
        else:
            if joystick_map['camera_reset']['used']: # If used on previous turn
                #video_dir.home_x_y()
                joystick_map['camera_reset']['used'] = False

    sleep(0.1)
