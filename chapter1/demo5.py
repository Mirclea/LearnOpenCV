import cv2


def show_image(windows_name, image):
    cv2.imshow(windows_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img1 = cv2.imread(r'../img/2.jpg')
    img2 = cv2.imread(r'../img/2-1.png')

    # show_image('0', img1)
    # res = cv2.resize(img1, (0, 0), fx=2, fy=1)
    # show_image('1', res)
    # res = cv2.resize(img1, (0, 0), fx=1, fy=2)
    # show_image('2', res)
    # res = cv2.resize(img1, (0, 0), fx=1.5, fy=1.5)
    # show_image('3', res)

    img2 = cv2.resize(img2, (1024, 576))
    print(img2.shape)
    print(img1.shape)
    #
    # img2 = img1 + 10
    #
    # print(img1[:5, :, 0])
    # print(img2[:5, :, 0])
    # print(img1.shape)
    #
    # img3 = img1 + img2
    # img4 = cv2.add(img1, img2)
    # print(img3[:5, :, 0])
    # print(img4[:5, :, 0])

    # show_image('1', img1)
    # show_image('2', img2)
    # show_image('3', img3)
    # show_image('4', img4)
    res = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
    show_image(" ", res)
