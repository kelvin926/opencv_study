import cv2
import numpy as np

img = cv2.imread("/Users/kelvin/Desktop/Coding/opencv_test/OpenCV 관련 파일들/opencv_study_example/image/marathon_01.jpg")
print("width : {}".format(img.shape[1]))
print("height : {}".format(img.shape[0]))
print("channels : {}".format(img.shape[2]))
(h, w) = img.shape[:2]

cv2.imshow("original", img)

face_cascade_name = "/Users/kelvin/Desktop/Coding/opencv_test/OpenCV 관련 파일들/ai_cv/haarcascades/haarcascade_frontalface_alt.xml"
eyes_cascade_name = "/Users/kelvin/Desktop/Coding/opencv_test/OpenCV 관련 파일들/ai_cv/haarcascades/haarcascade_eye_tree_eyeglasses.xml"

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()