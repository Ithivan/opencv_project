import cv2 as cv

img = cv.imread('image/test.jpg', 0)
cv.imshow('test image', img)

cv.waitKey(0)
cv.destroyAllWindows()
