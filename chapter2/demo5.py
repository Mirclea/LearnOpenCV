import numpy as np

import utils
import cv2

if __name__ == '__main__':
    pie = cv2.imread('../img/fs.png')
    pie = cv2.resize(pie, (200, 200))
    kernel = np.ones((7, 7), np.uint8)

    openNum = cv2.morphologyEx(pie, cv2.MORPH_OPEN, kernel)  # 开运算
    closeNum = cv2.morphologyEx(pie, cv2.MORPH_CLOSE, kernel)  # 闭运算
    gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)  # 梯度
    top = cv2.morphologyEx(pie, cv2.MORPH_TOPHAT, kernel)  # 礼帽
    black = cv2.morphologyEx(pie, cv2.MORPH_BLACKHAT, kernel)  # 黑帽

    res = utils.figure_splicing((pie, openNum, closeNum, gradient, top, black))
    utils.show_image('images result', res)
