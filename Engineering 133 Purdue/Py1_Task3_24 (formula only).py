# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

r = input("enter value for the radius: ")
#set input function for the radius

ri = float(r)
#make sure ri is a float, float is more flexible than integer in case the inserted number is not an integer


h = input("enter value for the height: ")
#set input function for the height

hi = float(h)
#make sure hi is a float, float is more flexible than integer in case the inserted number is not an integer


from math import pi,sqrt
#import the pi & square root function from math because its the only 2 we need

l = (sqrt((hi**2)+(ri**2)))
#calculate slant of cone as it is apart of the formula to find SA of cone

A = (pi*ri**2+pi*ri*l)

print (str(A)+'cm^2')
