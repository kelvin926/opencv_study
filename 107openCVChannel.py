import cv2
import numpy as np

print("OpenCV version:")
print(cv2.__version__)
 
img = cv2.imread("nomadProgramerIcon.png")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2]
center = (width // 2, height // 2)

cv2.imshow("nomadProgramer", img)

(Blue, Green, Red) = cv2.split(img) # BGR로 색 분리. 스플린트 한 다음에 BGR로 들어감.

cv2.imshow("Red Channel", Red) # 레드 영역만.
cv2.imshow("Green Channel", Green) # 그린 영역만.
cv2.imshow("Blue Channel", Blue) # 블루 영역만.
cv2.waitKey(0)

zeros = np.zeros(img.shape[:2], dtype = "uint8") # 제로필.
cv2.imshow("Red", cv2.merge([zeros, zeros, Red])) # 레드 필터
cv2.imshow("Green", cv2.merge([zeros, Green, zeros])) # 그린 필터
cv2.imshow("Blue", cv2.merge([Blue, zeros, zeros])) # 블루 필터
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 그레이 스케일
cv2.imshow("Gray Filter", gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # HSV 필터
cv2.imshow("HSV Filter", hsv)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) # LAB 필터
cv2.imshow("LAB Filter", lab)
cv2.waitKey(0)

BGR = cv2.merge([Blue, Green, Red]) # 색 다시 합쳐서 출력.
cv2.imshow("Blue, Green and Red", BGR)

cv2.waitKey(0)
cv2.destroyAllWindows()