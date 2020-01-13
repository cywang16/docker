import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

def getjpeghist(jpegfile, histjpeg):
    jpegobj = mpimg.imread(jpegfile)
    jpegnorm = jpegobj / 256.0
    res = plt.hist(jpegnorm[:, :, 0].ravel(), bins=512, range = (0, 0.99))
    print(len(res[1]))
    print(res[1][-1])
    plt.savefig(histjpeg)

getjpeghist(sys.argv[1], sys.argv[2])