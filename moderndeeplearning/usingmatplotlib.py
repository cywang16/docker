import numpy as np
import cv2
import matplotlib as mpl
mpl.use ('PDF')

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages('scratches.pdf')

img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
plt.savefig(pp, format='pdf')

pp.close()
