import cv2 as cv
import numpy as np
img = cv.imread(r"Resources\Photos\cat.jpg")
cv.imshow("cat", img)
cv.waitKey(0)
cv.destroyAllWindows()  # Ensure all windows are closed properly

# there ae 2 ways to draw on images 
#1. draw on the image itself 
#2. to make a dummy image to work with 
# to create a blank image 
blank = np.zeros((500,500,3), dtype='uint8') # uint8 is data type of an image .... np.zeros((500,500,3), dtype='uint8') .... (width, height, color channel)

cv.imshow("blank", blank)
cv.waitKey(0)
cv.destroyAllWindows()  # Ensure all windows are closed properly


# 1. paint the image to a certain color

# blank[:] = 0,255,0
# blank[:] mean it is refering to all the pixels .... full green image 
cv.imshow("green_blank", blank)
# blank[200:300 , 300:400] = 0,0,255
cv.imshow("partial_green_blank", blank)
cv.waitKey(0)
cv.destroyAllWindows()  # Ensure all windows are closed properly

# draw a recctangle

cv.rectangle(blank, (0,0),(250,250), (0,255,0), thickness=2)

# cv.rectangle(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED) 

# thickness=cv.FILLED means that the rectangle will be fully colored .... (blank.shape[1]//2, blank.shape[0]//2) means that end coordinates will be half of the width and height of the original image
# cv.rectangle(image, (start coordinate),(end coordinate), (color), thickness) 

# draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), (250,250) , 100, (0,0,255), thickness=3)



# draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2), (255,0,0), thickness=2 )
cv.imshow("line",blank)

# write text on an image

cv.putText(blank, "hello world", (225,225),cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0,255,0), thickness=2)
cv.imshow("text on the image", blank)
# if the text is not fitting the frame then we can do it by changing the position of the text


cv.imshow("rectangle", blank)
cv.waitKey(0)
cv.destroyAllWindows()  # Ensure all windows are closed properly