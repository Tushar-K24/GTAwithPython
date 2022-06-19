from mailbox import linesep
import numpy as np
import cv2

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def canny(img):
    median_pix = np.median(img)
    lower = int(max(0, 0.7*median_pix))
    upper = int(min(255, 1.3*median_pix))
    return cv2.Canny(img, threshold1=lower, threshold2=upper)

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass

def hough_transform(img):
    lines = cv2.HoughLinesP(img, rho=2, theta=np.pi/180, threshold=180, minLineLength=80, maxLineGap=50)
    return lines


def detect_lanes(img):

    #convert to grayscale
    processed_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    #blur the image
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)

    #detecting edges using canny
    processed_img = canny(processed_img)
    
    #masking roi
    vertices = np.array([[[10,600],[10,400],[300,200], [500,200], [800,400], [800,600]]])
    processed_img = roi(processed_img, vertices)

    #detecting straight lines
    lines = hough_transform(processed_img)

    #draw lines
    draw_lines(processed_img, lines)

    return processed_img