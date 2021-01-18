# Yujin.jpg 파일로 진행. 각 단계 마다 키를 눌러야지 진행되게 코딩.
import cv2
import numpy as np
# [1단계] opencv 버전 출력. 사진 출력. 사진의 너비와 높이 출력. 사진의 중심 좌표 출력.
print("버전은:"+ cv2.__version__)

img = cv2.imread("yujin.jpg")
cv2.imshow("yujin basic file", img)
yujin_height = img.shape[0]
yujin_width = img.shape[1]
yuzin_color_channel = img.shape[2]
if yuzin_color_channel == 3:
    yuzin_color_channel_text = "RGB"
else:
    yuzin_color_channel_text = "Unknown"
print("사진의 높이: {} , 사진의 너비: {} , 사진의 컬러 : {}".format(yujin_height, yujin_width, yuzin_color_channel_text))

center = (yujin_height//2, yujin_width//2) #나머지 반환. int형 출력.

print ("사진의 중심(x,y): ({},{})".format(center[0], center[1]))

cv2.waitKey(0)
cv2.destroyAllWindows()

# [1단계] jpg파일을 png파일로 변환하여 저장. 사진 중심의 색상 채널 값 출력. 사진 중심에 DOT화 하기, 점 부분만 따로 이미지 출력. 점 부분의 색 변환.
cv2.imwrite("yuzin_pngcvt.png", img)
print("파일을 png로 변환 완료! 해당 파일을 출력합니다!")

img_png = cv2.imread("yuzin_pngcvt.png")
cv2.imshow("png cvt photo", img_png)

(b, g, r) = img[center]
print("사진 중심의 RGB 값은-> RED: {}, GREEN: {}, BLUE: {}".format(r, g, b))

dot = img[center[0]-100:center[0]+100, center[1]-100:center[1]+100]

cv2.imshow("DOT", dot)

img[center[0]-100:center[0]+100, center[1]-100:center[1]+100] = (255,255,255)

cv2.imshow("dotted", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# [1단계] 사각형, 원, 선, 텍스트 각각 하나씩 그려서 출력.

cv2.rectangle(img, (100,100), (200,200), (255,0,255), thickness=5)

cv2.circle(img, (250,250), 50, (0,255,255), thickness=5)

cv2.line(img, (300,300), (500,500), (0,255,0), thickness=5)

cv2.putText(img, "yujin Hello!", (800,800), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,0), thickness=5)

cv2.imshow("DRAW", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# [1단계] 이미지를 위로,아래로,양옆으로 움직이게 해서 출력. 

# [1단계] 이미지를 회전. 이미지를 축소, 이미지를 확대.
# [1단계] 마스크를 만들고, 마스크와 마스크된 사진 출력.
# [1단계] 각각의 색 영역별로 출력. 여러 필터 적용해서 출력.
# [1단계] 각각의 색 영역별로 출력한 상태에 더 보기 편하도록 색 입혀서 출력.
# [1단계] 나눈 색 사진들을 조합하여 원본과 같은 사진 출력.