from concurrent.futures import process
import numpy as np
import cv2
import time
from PIL import ImageGrab
from directKeys import PressKey, ReleaseKey, W, A, S, D

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


def process_img(img):
    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=85, threshold2=255)
    return processed_img

last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600))) #x, y, w, h
    processed = process_img(screen)
    print('pressing')
    PressKey(0x11)
    time.sleep(3)
    ReleaseKey(0x11)
    print('released')
    print(f'loop took {time.time()-last_time}')
    cv2.imshow("window", processed)
    # cv2.imshow("window2", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    last_time = time.time()
    if cv2.waitKey(1) & 0Xff == ord('q'):
        cv2.destroyAllWindows()
        break
    