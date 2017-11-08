import numpy as np
import cv2
import os

messi5jpg = os.path.dirname(os.path.realpath(__file__)) + '/messi5.jpg'

# Load an color image in grayscale
img = cv2.imread(messi5jpg, 0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
