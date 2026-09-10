#accessing pixel values and modifying them
import cv2
import numpy as np

img='img.png'
image=cv2.imread(img)
px=img[100,100] #accessing pixel values
print(px) #prints the pixel values in BGR format

blue=img[100,100,0] #accessing blue pixel value
print(blue)

#modifying pixel values
img[100,100]=[255,255,255] #modifying pixel values to white

# image properties
print(img.shape) #returns a tuple of number of rows, columns and channels
print(img.size) #returns total number of pixels
print(img.dtype) #returns image datatype

# RGB, ARGB, HSV, YCrCb, Lab, Luv, HLS, XYZ, YUV formats

img_file='test.png'
img=cv2.imread(img_file,1) #1 for color, 0 for grayscale,
alpha_img=cv2.imread(img_file,-1) #-1 for unchanged, includes alpha channel
gray_img=cv2.imread(img_file,0) #grayscale

print('ARGB image shape:', alpha_img.shape)

#setting region of image- certain pixels to a certain value

cv2.selectROI(window_name='Select ROI', img=img, showCrosshair=True, fromCenter=False) #selecting region of interest

#cropping selected region
roi_cropped=img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] #cropping the selected region

cv2.imshow('Cropped ROI', roi_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
