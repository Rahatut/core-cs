#accessing pixel values and modifying them
import cv2
import numpy as np

img='img.png'
image=cv2.imread(img)

g,b,r = cv2.split(img) #splitting the channels of the image

cv2.imshow('Red Channel', r)
cv2.imshow('Green Channel', g)
cv2.imshow('Blue Channel', b)
cv2.waitKey(0)

cv2.merge((b,g,r)) #merging the channels back to form the original image
cv2.imshow('Merged Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.cvtColor(img, cv2.COLOR_RGB2LAB) #converting the image to LAB color space
cv2.imshow('LAB Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


src1=cv2.imread('test.png')
src2=cv2.imread('test.png')

# if needed, resize

cv2.addWeighted(src1, 0.7, src2, 0.3, 0) #blending two images together with specified weights

#0.7 and 0.3 are the weights for the two images, and 0 is the scalar added to each sum. The result is a new image that is a weighted combination of the two input images.

cv2.imshow('Blended Image', src1)
cv2.waitKey(0)  
cv2.destroyAllWindows()

# FILTERS & MASKING
kernel = np.array([[0, -1, 0], 
                   [-1, 9,-1], 
                   [0, -1, 0]]) #sharpening kernel
# playing with different kernels can produce different effects on the image, such as blurring, edge detection, embossing, etc.

cv2.filter2D(src1, -1, kernel) #applying a custom filter to the image using a kernel

cv2.imshow('Filtered Image', src1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image thresholding
ret, thresh1 = cv2.threshold(src1, 127, 255, cv2.THRESH_BINARY) #applying binary thresholding to the image
cv2.imshow('Binary Threshold', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()

canny = cv2.Canny(src1, 100, 200) #applying Canny edge detection to the image
cv2.imshow('Canny Edge Detection', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()