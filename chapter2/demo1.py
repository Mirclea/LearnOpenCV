import cv2
import utils

if __name__ == '__main__':
    img = cv2.imread('../img/pd.jpg')

    blur = cv2.blur(img, (3, 3))  # 均值滤波
    box = cv2.boxFilter(img, -1, (3, 3), normalize=False)  # 方框滤波
    gaussian = cv2.GaussianBlur(img, (5, 5), 1)  # 高斯滤波
    median = cv2.medianBlur(img, 5)  # 中值滤波

    # utils.show_image('0', img)
    # utils.show_image('1', blur)
    # utils.show_image('2', box)
    # utils.show_image('3', gaussian)
    # utils.show_image('4', median)

    res = utils.figure_splicing((img, blur, gaussian, median))
    utils.show_image('r', res)
