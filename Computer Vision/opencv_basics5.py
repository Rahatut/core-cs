import cv2
import numpy as np
import matplotlib.pyplot as plt

#contour detection and shape detection
img = cv2.imread('test.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting to grayscale
#blur = cv2.GaussianBlur(gray, (5, 5), 0)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

 
for contour in contours: 
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True) #approximating the contour to a polygon
    cv2.drawContours(img, [approx], 0, (0, 0, 255), 5) #drawing the contour on the image


    #finding centre of the contour
    M = cv2.moments(contour) #calculating the moments of the contour
    if M['m00'] != 0: #if the area of the contour is not zero
        cx = int(M['m10'] / M['m00']) #calculating the x coordinate of the centre
        cy = int(M['m01'] / M['m00']) #calculating the y coordinate of the centre
        cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1) #drawing a circle at the centre of the contour        

    x = approx.ravel()[0] #getting the x coordinate of the first point of the contour
    y = approx.ravel()[1] #getting the y coordinate of the first point of the contour

    if len(approx) == 3: #if the contour has 3 points, it is a triangle
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    elif len(approx) == 4: #if the contour has 4 points, it is a rectangle or square
        x1, y1, w, h = cv2.boundingRect(approx) #getting the bounding rectangle of the contour
        aspectRatio = float(w) / h #calculating the aspect ratio
        if aspectRatio >= 0.95 and aspectRatio <= 1.05: #if the aspect ratio is close to 1, it is a square
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else: #otherwise it is a rectangle
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    elif len(approx) == 5: #if the contour has 5 points, it is a pentagon
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    elif len(approx) == 6: #if the contour has 6 points, it is a hexagon
        cv2.putText(img, "Hexagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)          

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#color detection
#HSV color space is a cylindrical color model that represents colors in terms of their hue, saturation, and value (brightness).
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #converting the image to HSV color space

lower_blue = np.array([100, 50, 50]) #lower bound of blue color in HSV
upper_blue = np.array([140, 255, 255]) #upper bound of blue color in HSV
mask = cv2.inRange(hsv, lower_blue, upper_blue) #creating a mask for blue color
res = cv2.bitwise_and(img, img, mask=mask) #applying the mask to the image
cv2.imshow('Mask', mask)
cv2.imshow('Result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()