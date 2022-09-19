import cv2
import utils
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../img/fs.png')
    img = cv2.resize(img, (200, 200))
    kernel1 = np.ones((5, 5), np.uint8)
    kernel2 = np.ones((3, 3), np.uint8)
    kernel3 = np.ones((7, 7), np.uint8)
    erosion1 = cv2.erode(img, kernel1, iterations=1)
    erosion2 = cv2.erode(img, kernel1, iterations=2)
    erosion3 = cv2.erode(img, kernel1, iterations=3)

    erosion33 = cv2.erode(img, kernel2, iterations=1)
    erosion55 = erosion1
    erosion77 = cv2.erode(img, kernel3, iterations=1)

    res1 = utils.figure_splicing((img, erosion1, erosion2, erosion3))
    utils.show_image("iterations", res1)

    res2 = utils.figure_splicing((img, erosion33, erosion55, erosion77))
    utils.show_image("kernel_size", res2)

