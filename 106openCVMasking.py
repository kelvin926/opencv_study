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

mask = np.zeros(img.shape[:2], dtype = "uint8")  # 제로 필 된 넘파이 행렬.

cv2.circle(mask, center, 300, (255, 255, 255), -1) # 마스크에다가 원으로 된 가득 찬 흰색 마스크 생성. (검은색 제로필에 흰색 원 생성.)

cv2.imshow("mask", mask)
 
masked = cv2.bitwise_and(img, img, mask = mask) # and 연산자. 합친다!! / 검은색 부분은 false값 이므로, and 연산에서 제외. so, 둘 다 true (흰색, 그림) 부분만 보이게 됨.
# or이라도, 마스크가 가려버리는 듯.
cv2.imshow("nomadProgramer with mask", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()