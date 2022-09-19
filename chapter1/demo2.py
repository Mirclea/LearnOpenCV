import cv2

if __name__ == "__main__":

    vc = cv2.VideoCapture(r'../img/1.mp4')
    if vc.isOpened():
        opened, frame = vc.read()
    else:
        opened = False
    while opened:
        ret, frame = vc.read()
        if frame is None:
            break
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('result',gray)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    vc.release()
    cv2.destroyAllWindows()

    # print(frame.shape)
