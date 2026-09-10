#cv2.IMREAD_COLOR or 1, gray to col
#cv2.IMREAD_GRAYSCALE or 0
#cv2.IMREAD_UNCHANGED or -1

import cv2

img = cv2.imread("test.png")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("test.png", 1)
img = cv2.imread("test.png", 0)
img = cv2.imread("test.png", -1)

#playing webcam vd

capture = cv2.VideoCapture(0)

#while True:
    #ret, frame = capture.read()
    #cv2.imshow("Webcam", frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'): #key pressed to quit
        #break

capture.release()
cv2.destroyAllWindows()

#saving video
if(capture.isOpened() == False):
    print("Error opening video stream or file")

frame_w=int(capture.get(3))
frame_h=int(capture.get(4))

#encoders and decoders for video compression and decompression. FourCC is a 4-byte code used to specify the video codec. 
# It is used in video file formats to indicate the codec used to compress the video data. The FourCC code is typically represented as a string of four characters, 
# such as 'XVID', 'MJPG', or 'H264'. Each character in the code corresponds to a specific byte value, and together they uniquely identify the codec.

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.MP4', fourcc, 20.0, (frame_w, frame_h)) #fourcc is the 4 char code that specifies the video codec

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        # Write the frame into the file 'output.MP4'
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything
capture.release()
out.release()
cv2.destroyAllWindows()

