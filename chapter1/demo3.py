import cv2


def show_image(windows_name, image):
    cv2.imshow(windows_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image = cv2.imread(r'../img/2.jpg')

    cur_img = image.copy()
    cur_img[:, :, 2] = 0
    cur_img[:, :, 0] = 0
    show_image('r', cur_img)
