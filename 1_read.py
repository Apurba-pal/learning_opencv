import cv2 as cv

img = cv.imread("image.png")
# cv.imread(name of the  window/frame, variable name)
img = cv.imshow('Cat', img)
cv.waitKey(0)
# waitkey is a keyboard binding function which waits for a specific delay (time in miliseconds) for a key to be pressed ... if you pass 0 it waits for an infinite amount of time for a keybooard key to be pressed






# for videos 
capture = cv.VideoCapture("videos/dog.mp4")

# this method takes an integer like 0,1,2 (if you have a webcam) or a video path 
# the capture variable is an instance of this video capture class

while True:
    # here we grab the video frame by frame by utilising the capture.read() method 
    IsTrue, frame = capture.read()
    # reads the video frame by frame and a boolean which says that whether it was successfully read or not
    cv.imshow('Video', frame)
    # display each frame by this cv.imshow('Video', frame) code
    # to break out of this loop 
    if cv.waitKey(20) & 0xFF==ord('d'): # this basically says that if D is presses then stop the loop 
        break

capture.release()
cv.destroyAllWindows()

# (-215:Assertion faied) this errors occurs when cv could not find any more frames (in case of video ) or could not find any image you provided in the path (in case of image if you provide wrong address)