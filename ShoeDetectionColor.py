"""
Name: ShoeDetectionColor
Author: Gentry Darkins, Malique Akbar, Kowe Kadoma
Purpose: Detect shoe with color segmentation
Date: March 5, 2021
Functional: Works
Future improvements:
"""

from moviepy.editor import *
#from moviepy.video.fx.all import crop
import cv2
import ffmpeg
import numpy as np
import matplotlib.pyplot as plt
#import imtils
from matplotlib import cm
from matplotlib import colors

#Reading in the video
file = cv2.VideoCapture("Trial 17.MP4")
"""
#Determining the ranges for color segmentation
success,image = vidcap.read()
count = 0
#reading in frame by frame
while success: 
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

frame = cv2.imread('frame217.jpg')
cropped_frame = frame[260:440, 0:2704]
hsv_frame= cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2HSV)

#visualizing the rbg of frame
r, g, b = cv2.split(cropped_frame)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")
pixel_colors = frame.reshape((np.shape(frame)[0]*np.shape(frame)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()

#visualizing hsv
h, s, v = cv2.split(hsv_frame)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")
axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()

#determining color range of frame
#30, 52, 72 to 50,130,255 will mask of the background
lower = np.array([37, 52, 72])
upper = np.array([50,150,255]) 
mask = cv2.inRange(hsv_frame, lower, upper)
result = cv2.bitwise_and(cropped_frame,cropped_frame, mask=mask)
plt.subplot(1, 2, 1)
plt.imshow(cropped_frame, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()
"""

while (file.isOpened()):
   ret, frame = file.read()
   cropped_frame = frame[260:440, 0:2704]
   hsv_frame= cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2HSV)

   #Marker Color Range
   low_mark=np.array([37, 52, 72])
   high_mark=np.array([50,150,255])
   mask=cv2.inRange(hsv_frame, low_mark, high_mark)
   result = cv2.bitwise_and(hsv_frame, hsv_frame, mask=mask)

   cv2.imshow("Window",result) #originally mask
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
