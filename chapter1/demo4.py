import cv2
import matplotlib.pyplot as plt


def show_image(windows_name, image):
    cv2.imshow(windows_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread(r'../img/2.jpg')

    top, right, left, bottom = (50, 50, 50, 50)

    replicate = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_CONSTANT, value=10)

    show_image('0', img)
    show_image('1', replicate)
    show_image('2', reflect)
    show_image('3', reflect101)
    show_image('4', wrap)
    show_image('5', constant)
