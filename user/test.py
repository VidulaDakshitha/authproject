import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX

# Load the image
image = cv2.imread('1.png')

# making image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# thresholding the gray image, then white => black, black => white
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# getting the contours of dilate image
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0]
    # if len(cnts) == 2 else cnts[1]

count = 0
length = len(cnts)
for cnt in cnts:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    a = approx.ravel()[0]
    b = approx.ravel()[1]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Green with questions and Red with answers', image)
cv2.waitKey(0)
cv2.destroyAllWindows()