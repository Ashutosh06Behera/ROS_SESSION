#!/usr/bin/env python3

import rospy
import turtle

t = turtle.Turtle()

l = 100
w = 200

# drawing first side
t.forward(l) # Forward turtle by l units
t.left(90) # Turn turtle by 90 degree

# drawing second side
t.forward(w) # Forward turtle by w units
t.left(90) # Turn turtle by 90 degree

# drawing third side
t.forward(l) # Forward turtle by l units
t.left(90) # Turn turtle by 90 degree

# drawing fourth side
t.forward(w) # Forward turtle by w units
t.left(90) # Turn turtle by 90 degree

