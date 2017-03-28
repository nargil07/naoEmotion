# Standard scientific Python imports
from naoqi import ALProxy
#
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
s, im = vc.read() # captures image
cv2.imshow("Test Picture", im) # displays captured image
cv2.imwrite("test.bmp",im) # writes image test.bmp to disk