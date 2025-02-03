# 5 essential functions

import cv2 as cv
img = cv.imread(r"Resources\Photos\cat.jpg")
cv.imshow("cat", img)
cv.waitKey(0)
cv.destroyAllWindows()