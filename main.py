from grabScreen import grab_screen
import numpy as np
import cv2
import time

from directKeys import PressKey, ReleaseKey, W, A, S, D
from detectLanes import detect_lanes

def main():
    last_time = time.time()
    while True:
        screen = grab_screen(region=(0,40,800,640))
        processed = detect_lanes(screen)
        # print('pressing')
        # PressKey(0x11)
        # time.sleep(3)
        # ReleaseKey(0x11)
        # print('released')
        print(f'loop took {time.time()-last_time}')
        cv2.imshow("window", processed)
        # cv2.imshow("window2", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        last_time = time.time()
        if cv2.waitKey(1) & 0Xff == ord('q'):
            cv2.destroyAllWindows()
            break
        
main()