import cv2
import utils

if __name__ == '__main__':
    img = cv2.imread('../img/2.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(300,300))
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobely = cv2.convertScaleAbs(sobely)
    sobelxy1 = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    sobelxy2 = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
    sobelxy2 = cv2.convertScaleAbs(sobelxy2)

    res = utils.figure_splicing((img, sobelx, sobely, sobelxy1, sobelxy2))

    utils.show_image('res', res)
