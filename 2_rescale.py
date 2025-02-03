# we resize and rescale files to prevent computational strain.
import cv2 as cv


# resizing the image

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale) # frame.shape[1] is for the width of the image 
    height = int(frame.shape[0]*scale) # frame.shape[0] is for the height of the image 
    dimensions = (width, height) # just created a tupple so that it is easy to pass the data 
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



img = cv.imread("image.png")
cv.imshow("image", img)
rescaled_image = rescaleFrame(img)
cv.imshow("rescaled image", rescaled_image)

cv.waitKey(0)
cv.destroyAllWindows()