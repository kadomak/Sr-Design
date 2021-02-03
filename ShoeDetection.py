"""
Name: ShoeDetection
Author: Gaby Nelson, Kowe Kadoma
Purpose: To identify the shoe in the video
Date: Feb 3, 2021
Functional: Somewhat
Challenges: Errors with certain videos
"""
#Imports
import numpy as np
import cv2
import imutils

#Function Definitions
def Canny_detector(img, weak_th=None, strong_th=None): #Modified Canny operator
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Conversion of image to grayscale
    img = cv2.bilateralFilter(img, 15, 75, 75) #Noise reduction step

    gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3) #Calculating the gradients
    gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)

    mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True) #Conversion of Cartesian coordinates to polar

    mag_max = np.max(mag) # setting the minimum and maximum thresholds for double thresholding
    if not weak_th: weak_th = mag_max * 0.1
    if not strong_th: strong_th = mag_max * 0.5

    height, width = img.shape # getting the dimensions of the input image

    for i_x in range(width): # Looping through every pixel of the grayscale image
        for i_y in range(height):

            grad_ang = ang[i_y, i_x]
            grad_ang = abs(grad_ang - 180) if abs(grad_ang) > 180 else abs(grad_ang)

            if grad_ang <= 22.5:  # selecting the neighbours of the target pixel according to the gradient direction in the x axis direction
                neighb_1_x, neighb_1_y = i_x - 1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y

            elif grad_ang > 22.5 and grad_ang <= (22.5 + 45): #top right (diagnol-1) direction
                neighb_1_x, neighb_1_y = i_x - 1, i_y - 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y + 1

            elif grad_ang > (22.5 + 45) and grad_ang <= (22.5 + 90): #In y-axis direction
                neighb_1_x, neighb_1_y = i_x, i_y - 1
                neighb_2_x, neighb_2_y = i_x, i_y + 1

            elif grad_ang > (22.5 + 90) and grad_ang <= (22.5 + 135): #top left (diagnol-2) direction
                neighb_1_x, neighb_1_y = i_x - 1, i_y + 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y - 1

            elif grad_ang > (22.5 + 135) and grad_ang <= (22.5 + 180): #Now it restarts the cycle
                neighb_1_x, neighb_1_y = i_x - 1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y

            if width > neighb_1_x >= 0 and height > neighb_1_y >= 0: # Non-maximum suppression step
                if mag[i_y, i_x] < mag[neighb_1_y, neighb_1_x]:
                    mag[i_y, i_x] = 0
                    continue

            if width > neighb_2_x >= 0 and height > neighb_2_y >= 0:
                if mag[i_y, i_x] < mag[neighb_2_y, neighb_2_x]:
                    mag[i_y, i_x] = 0

    weak_ids = np.zeros_like(img)
    strong_ids = np.zeros_like(img)
    ids = np.zeros_like(img)

    for i_x in range(width): # double thresholding step
        for i_y in range(height):

            grad_mag = mag[i_y, i_x]

            if grad_mag < weak_th:
                mag[i_y, i_x] = 0
            elif strong_th > grad_mag >= weak_th:
                ids[i_y, i_x] = 1
            else:
                ids[i_y, i_x] = 2

    return mag # finally returning the magnitude of gradients of edges



#Main program
cap = cv2.VideoCapture("Trial 3.MP4") # Creating a VideoCapture object to read the video

while (cap.isOpened()): # Loop until the end of the video
    ret, frame = cap.read() # Capture frame-by-frame
    cropped_frame = frame[260:440,0:2704] #crop frame to only see feet and markers

    cropped_frame = cv2.resize(cropped_frame, (540, 380), fx=0, fy=0, interpolation=cv2.INTER_AREA) # Display the resulting frame
    cv2.imshow('Frame', cropped_frame)

    edge_detect = Canny_detector(cropped_frame) #applying modified canny operator
    cv2.imshow('Edge detect', edge_detect)

    if cv2.waitKey(25) & 0xFF == ord('q'): #define q as the exit button
        break


cap.release() # release the video capture object

cv2.destroyAllWindows() # Closes all the windows currently opened.
