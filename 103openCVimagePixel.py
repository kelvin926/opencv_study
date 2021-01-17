import cv2

print("OpenCV version:")
print(cv2.__version__)
 
img = cv2.imread("nomadProgramerIcon.png")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))
 
cv2.imshow("nomadProgramer", img) # 이미지 쇼
 
(b, g, r) = img[0, 0] # 주의!!!!!!!!!!! RGB값을 openCV는 BGR순서로 가지고 온다!! (픽셀) [왼쪽 최상단 픽셀을 가지고 옴.]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

dot = img[50:100, 50:100] # 50~100, 50~100 픽셀을 DOT 화 함.
cv2.imshow("Dot", dot) # 이미지 쇼 (DOT)

img[50:100, 50:100] = (0, 0, 255) # RED = 255 , DOT 부분을 레드로 채움.

cv2.imshow("nomadProgramer -dotted", img) # DOT 부분 빨갛게 칠해진 사진 쇼.

cv2.waitKey(0)
cv2.destroyAllWindows()
