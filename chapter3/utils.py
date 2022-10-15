import cv2
import numpy as np


def show_image(windows_name, image):
    cv2.imshow(windows_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def figure_splicing(images):
    res = np.hstack(images)
    return res