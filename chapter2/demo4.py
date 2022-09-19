import numpy as np

import utils
import cv2

if __name__ == '__main__':
    pie = cv2.imread('../img/pi.png')
    kernel = np.ones((7, 7), np.uint8)
    dilate = cv2.dilate(pie, kernel, iterations=5)
    erosion = cv2.erode(pie, kernel, iterations=5)

    gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)

    res = utils.figure_splicing((pie, dilate, erosion, gradient))
    utils.show_image("images", res)
