import cv2


def show_image(windows_name, image):
    cv2.imshow(windows_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image1 = cv2.imread(r'../img/2.jpg')
    image2 = cv2.imread(r'../img/2.jpg', cv2.IMREAD_GRAYSCALE)
    print(image1.shape)
    print(image2.shape)
    show_image('img1', image1)
    show_image('img2', image2)