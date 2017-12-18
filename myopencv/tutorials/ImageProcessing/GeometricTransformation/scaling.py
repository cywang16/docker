import numpy as np
import cv2 as cv

img = cv.imread('../../GuiFeaturesInOpenCV/messi5.jpg')
# img = cv.imread('messi5.jpg')
print(img)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
height, width = img.shape[:2]
print(height)
print(width)

res = cv.resize(img, (2*width, 2*height), interpolation = cv.INTER_CUBIC)
print(img)
cv.imshow('image', res)
cv.waitKey(0)
cv.destroyAllWindows()

rows, cols = img.shape[:2]
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
