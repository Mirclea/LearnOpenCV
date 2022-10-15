import cv2
import utils

if __name__ == '__main__':
    img = cv2.imread('../img/2.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (600, 400))
    v1 = cv2.Canny(img, 80, 150)
    v2 = cv2.Canny(img, 50, 100)

    res = utils.figure_splicing((v1, v2))
    utils.show_image("11", res)
