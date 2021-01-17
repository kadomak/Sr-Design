"""
Name: TrackExtraction
Author: Kowe Kadoma
Purpose: To create the lines of best fit on the track
Date: Jan 16, 2021
Functional: not yet tested
Challenges:
"""
#Imports
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Loading the video
img = cv2.imread("lenna.png")

#Cropping frame of track video
x,y,h,w=100
"""
These are just dummy variables to hold the dimensions
how do we know the dimensions which are exact to focus on the track 
& what is the margin of error?
"""
img = img[y:y+h, x:x+w]

#Histogram equalization operation
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting to B&W
dst = cv2.equalizeHist(img)

#Gaussian filter
img = cv2.GaussianBlur(img,(5,5),0)

#Converting to binary image
img = cv2.threshold(img,cv2.THRESH_BINARY)

#Canny operator to extract edges

#Counting the number of markers

#Connecting using line of best fit
