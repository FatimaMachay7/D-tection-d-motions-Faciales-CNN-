import cv2
img = cv2.imread('girl.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)