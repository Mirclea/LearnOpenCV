import cv2
import numpy as np

import utils

if __name__ == '__main__':
    img = cv2.imread('../img/pi.png', cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(img, kernel, iterations=10)
    res1 = utils.figure_splicing((img, dilate))
    utils.show_image(" ", res1)

    # 开运算
    j0 = img = cv2.imread('../img/fs.png')
    kernel1 = np.ones((3, 3), np.uint8)
    j1 = cv2.erode(j0, kernel1, iterations=10)
    j2 = cv2.dilate(j1, kernel1, iterations=10)
    res2 = utils.figure_splicing((j0, j1, j2))
    utils.show_image("process", res2)

    # 闭运算
    kernel2 = np.ones((3, 3), np.uint8)
    ji1 = cv2.dilate(j0, kernel2, iterations=10)
    ji2 = cv2.erode(ji1, kernel2, iterations=10)
    res3 = utils.figure_splicing((j0, ji1, ji2))
    utils.show_image("process", res3)
