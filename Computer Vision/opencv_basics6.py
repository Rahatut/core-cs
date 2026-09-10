import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.png')

# replacement of roi in 2D

img1 = cv2.imread('test.png')

mask=np.zeros((100,300,3), np.uint8) #creating a mask of zeros rxc

print(mask.shape)

pos=(200,200) #position where the object will be placed
var=img1[200:(200+mask.shape[0]), 200:(200+mask.shape[1])] = mask
#region of interest in the image where the object will be placed
cv2.imshow('Color replacement', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()