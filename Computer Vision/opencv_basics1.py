path = 'img.png'
window_name = 'Image'
directory = 'place'
filename = 'output.png'
start = (100, 100)
end = (300, 300)
centre = (630, 200)
axes_length = (120, 80)
angle_start = 0
angle_end = 360
thickness = 5

import cv2

image = cv2.imread(path)

cv2.imshow(window_name, image)

cv2.waitKey()
cv2.destroyAllWindows()

#instance on screen
cv2.imwrite(filename, image)
print("Success")

print(image.shape) #info on resolution

#row, col, color vals, rgb space, 3 channel space
#ycvcr for face recognition

cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.cvtColor(image,cv2.COLOR_GRAY2RGB) #greyscale

#img resizing
cv2.resize(image, (800,800))

cv2.putText(image, 'OpenCV', (500,500),cv2.FONT_HERSHEY_SIMPLEX, 4, (255,0,0),2)
#displays opencv text in red. last one is font thickness

cv2.line(image, (500,400), (900,500), (0,0,255),5)
#start, end, thick, col

cv2.circle(image, (630,200), 80, (0,0,255),5)
# centre, radius, col, thickness

cv2.rectangle(image, start, end, (0,0,255),5)

cv2.ellipse(image, centre, axes_length, angle_start, angle_end, (0,0,255),thickness)