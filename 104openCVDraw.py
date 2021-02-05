#-*-coding:utf-8-*-

import cv2

print("OpenCV version:")
print(cv2.__version__)

img = cv2.imread("nomadProgramerIcon.png")
print("너비: {} pixels".format(img.shape[1]))
print("높이: {} pixels".format(img.shape[0]))
print("색 채널: {}".format(img.shape[2]))

cv2.imshow("nomadProgramer", img)

(b, g, r) = img[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

dot = img[50:100, 50:100]

img[50:100, 50:100] = (0, 0, 255) # x: 50~100, y: 50~100 부분을 RED 로 채움.

cv2.rectangle(img, (100, 00), (300, 200), (0, 255, 0), 5) # 사각형. (이미지, (사각형의 왼쪽 위 X,Y), (사각형의 오른쪽 아래 X,Y) (B,G,R), 선 굵기)

cv2.circle(img, (275, 75), 25, (0, 255, 255), -1) # 원. (이미지, (중앙 x,y), 반지름, (b,g,r), 선 굵기[음수일 경우 채움])

cv2.line(img, (350, 100), (400, 100), (255, 0, 0), 5) # 선. (이미지, (첫 x,y), (둘 x,y), (b,g,r), 굵기 [선의 경우 음수의 굵기를 가질 수 없음.])

cv2.putText(img, 'kelvin!', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4) # 텍스트. (이미지, '문자열', (왼쪽하단 x,y 좌표), 폰트, 폰트 크기, (b,g,r), 굵기)

cv2.imshow("kelvin - draw", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
