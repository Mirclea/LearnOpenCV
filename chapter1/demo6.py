import cv2
import matplotlib.pyplot as plt


def show_image(windows_name, image):
    cv2.imshow(windows_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('../img/2.jpg', cv2.IMREAD_GRAYSCALE)

    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    # show_image('0', img)
    # show_image('1', thresh1)
    # show_image('2', thresh2)
    # show_image('3', thresh3)
    # show_image('4', thresh4)
    # show_image('5', thresh5)
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    names = ["0", "THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC", "THRESH_TOZERO", "THRESH_TOZERO_INV"]
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], "gray")
        plt.title(names[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
